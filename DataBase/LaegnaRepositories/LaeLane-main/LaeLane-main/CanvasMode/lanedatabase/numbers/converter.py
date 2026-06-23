import os
import json

from laepng import LaePNG
from laesvg import LaeSVG
from laejson import LaeJSON

R_FOLDERS = ["0.5", "1", "2", "3", "4"]

MODES = {
    "SigLae": ("Ten", "Signed"),
    "UnsigLae": ("Ten", "UnSigned"),
    "SigDec": ("Dec", "Signed"),
    "UnsigDec": ("Dec", "UnSigned"),
}

MODE_SUFFIX = {
    "SigLae": "_st",
    "UnsigLae": "_ut",
    "SigDec": "_sd",
    "UnsigDec": "_ud",
}

VERBOSE = True
LOGFILE = "converter.log"


def log(msg: str) -> None:
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    if VERBOSE:
        print(msg)


with open(LOGFILE, "w", encoding="utf-8") as f:
    f.write("=== Converter run started ===\n")


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_points_mode(data, axe: str, sign: str):
    pts = []
    keys = sorted(
        [k for k in data.keys() if k.isdigit()],
        key=lambda k: int(k)
    )
    for idx in keys:
        node = data[idx]
        try:
            x = node[axe][sign]["X"]
            y = node[axe][sign]["Y"]
        except KeyError:
            continue
        pts.append((int(x), int(y)))
    return pts


def laegna_to_pixel(x: int, y: int, b: dict):
    i = x - b["minX"]
    j = y - b["minY"]
    return i, j


def pixel_to_center(i: int, j: int, b: dict):
    # x_center = x + 0.5, y_center = y + 0.5
    x = b["minX"] + i + 0.5
    y = b["minY"] + j + 0.5
    return x, y


def compute_boundaries():
    """
    Per-R+mode shared bounds:
    - minX, maxX, minY, maxY from ALL glyphs in that R+mode.
    - widthSquares  = (maxX - minX) + 1
    - heightSquares = (maxY - minY) + 1
    """
    boundaries = {"R": {}}

    for r in R_FOLDERS:
        log(f"Scanning R folder: {r}")
        if not os.path.isdir(r):
            log(f"  WARNING: folder {r} does not exist, skipping")
            continue

        try:
            files = os.listdir(r)
        except Exception as e:
            log(f"  ERROR reading folder {r}: {e}")
            continue

        boundaries["R"][r] = {
            "Modes": {},
            "WidthSquares": None,
            "HeightSquares": None,
        }

        for mode_name, (axe, sign) in MODES.items():
            all_pts = []

            for fname in files:
                if not fname.startswith("L"):
                    continue
                if not fname.lower().endswith(".json"):
                    continue

                fpath = os.path.join(r, fname)
                try:
                    data = load_json(fpath)
                except Exception:
                    continue

                pts = extract_points_mode(data, axe, sign)
                all_pts.extend(pts)

            if not all_pts:
                continue

            xs = [p[0] for p in all_pts]
            ys = [p[1] for p in all_pts]

            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)

            width = (max_x - min_x) + 1
            height = (max_y - min_y) + 1
            if width <= 0:
                width = 1
            if height <= 0:
                height = 1

            boundaries["R"][r]["Modes"][mode_name] = {
                "minX": min_x,
                "maxX": max_x,
                "minY": min_y,
                "maxY": max_y,
                "widthSquares": width,
                "heightSquares": height,
                "projection": [[1, 0], [0, 1]],
                "explanation": (
                    "Per-R+mode shared bounds. "
                    "Squares are unit length. "
                    "Pixel index i = x - minX, j = y - minY. "
                    "Center = x + 0.5, y + 0.5. "
                    "Canvas size = (max - min) + 1 to include all pixels."
                ),
            }

        ws = []
        hs = []
        for m in boundaries["R"][r]["Modes"].values():
            ws.append(m["widthSquares"])
            hs.append(m["heightSquares"])

        if ws and hs:
            boundaries["R"][r]["WidthSquares"] = max(ws)
            boundaries["R"][r]["HeightSquares"] = max(hs)

    with open("boundaries.json", "w", encoding="utf-8") as f:
        json.dump(boundaries, f, indent=4)
    log("Wrote boundaries.json")

    lines = []
    lines.append("# LaeLane Boundaries\n")
    for r, rdata in boundaries["R"].items():
        lines.append(f"## R={r}\n")
        lines.append(f"- Global width (squares): {rdata['WidthSquares']}")
        lines.append(f"- Global height (squares): {rdata['HeightSquares']}\n")
        for mode_name, b in rdata["Modes"].items():
            lines.append(f"### Mode {mode_name}\n")
            lines.append(f"- minX: {b['minX']}")
            lines.append(f"- maxX: {b['maxX']}")
            lines.append(f"- minY: {b['minY']}")
            lines.append(f"- maxY: {b['maxY']}")
            lines.append(f"- widthSquares: {b['widthSquares']}")
            lines.append(f"- heightSquares: {b['heightSquares']}")
            lines.append(f"- projection: [[1,0],[0,1]]")
            lines.append(f"- explanation: {b['explanation']}\n")

    with open("boundaries.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    log("Wrote boundaries.md")

    return boundaries


def generate_all(boundaries: dict):
    gen_record = []
    readme = []

    for r in R_FOLDERS:
        if not os.path.isdir(r):
            continue

        rdata = boundaries["R"].get(r)
        if not rdata:
            continue

        modes_bound = rdata["Modes"]

        try:
            files = os.listdir(r)
        except Exception as e:
            log(f"  ERROR reading folder {r}: {e}")
            continue

        for fname in files:
            if not fname.startswith("L"):
                continue
            if not fname.lower().endswith(".json"):
                continue

            fpath = os.path.join(r, fname)
            try:
                data = load_json(fpath)
            except Exception:
                continue

            base = os.path.splitext(fname)[0]
            num = base[1:] if base.startswith("L") else base

            readme.append(f"# {num} (R={r})\n")

            for mode_name, (axe, sign) in MODES.items():
                b = modes_bound.get(mode_name)
                if not b:
                    continue

                pts_lae = extract_points_mode(data, axe, sign)
                if not pts_lae:
                    continue

                pts_pix = [laegna_to_pixel(x, y, b) for (x, y) in pts_lae]

                readme.append(f"## {num} / {mode_name}\n")
                for i, (x, y) in enumerate(pts_lae, 1):
                    readme.append(f"- Laegna {i}: ({x}, {y})")
                for i, (pi, pj) in enumerate(pts_pix, 1):
                    readme.append(f"  - Pixel {i}: ({pi}, {pj})")

                suffix = MODE_SUFFIX[mode_name]
                width = b["widthSquares"]
                height = b["heightSquares"]

                # PNG: one pixel per square, Bresenham connectivity
                png_name = f"{num}{suffix}.png"
                png = LaePNG(png_name, r, width, height)
                png.draw_polyline(pts_pix)
                png.save()

                # SVG: integer coordinates, Bresenham connectivity
                svg_name = f"{num}{suffix}.svg"
                svg = LaeSVG(svg_name, r, width, height, b["minX"], b["minY"])
                svg.draw_polyline(pts_lae, b)

                # JSON + CSV: pixel indices + centers
                json_name = f"{num}{suffix}.json"
                jj = LaeJSON(json_name, r, width, height)
                for (x, y), (pi, pj) in zip(pts_lae, pts_pix):
                    x_center = x + 0.5
                    y_center = y + 0.5
                    jj.add_point(pi, pj, x_center, y_center)
                jj.save()

                gen_record.append(
                    f"{num}{suffix} generated in R={r}, mode={mode_name}, "
                    f"width={width}, height={height}"
                )

    with open("gen_record.md", "w", encoding="utf-8") as f:
        f.write("\n".join(gen_record))
    log("Wrote gen_record.md")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(readme))
    log("Wrote README.md")


def main():
    boundaries = compute_boundaries()
    generate_all(boundaries)
    log("=== Converter run finished ===")


if __name__ == "__main__":
    main()
