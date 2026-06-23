import os
from xml.etree.ElementTree import Element, SubElement, ElementTree


class LaeSVG:
    def __init__(self, filename: str, r: str, width: int, height: int, min_x: int, min_y: int):
        self.r = r
        self.filename = filename
        self.width = int(width)      # units
        self.height = int(height)
        self.min_x = int(min_x)
        self.min_y = int(min_y)

    def _bresenham_line(self, p0, p1, svg):
        x0, y0 = p0
        x1, y1 = p1
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        # Build path with integer coordinates
        d = []
        while True:
            d.append(f"L {x0} {y0}" if d else f"M {x0} {y0}")
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

        SubElement(
            svg,
            "path",
            {
                "d": " ".join(d),
                "stroke": "black",
                "fill": "none",
                "stroke-width": "1",  # 1 unit
            },
        )

    def draw_polyline(self, pts_lae, bounds):
        os.makedirs(self.r, exist_ok=True)
        path = os.path.join(self.r, self.filename)

        svg = Element(
            "svg",
            {
                "xmlns": "http://www.w3.org/2000/svg",
                "version": "1.1",
                "width": f"{self.width}cm",
                "height": f"{self.height}cm",
                "viewBox": f"{self.min_x} {self.min_y} {self.width} {self.height}",
            },
        )

        # Optional: black background
        SubElement(
            svg,
            "rect",
            {
                "x": str(self.min_x),
                "y": str(self.min_y),
                "width": str(self.width),
                "height": str(self.height),
                "fill": "white",
            },
        )

        if not pts_lae:
            tree = ElementTree(svg)
            tree.write(path, encoding="utf-8", xml_declaration=True)
            return

        # Map Laegna integer coords to integer SVG coords:
        # svg_x = (x - minX) + 0.5, rounded
        # svg_y = (y - minY) + 0.5, rounded
        min_x = bounds["minX"]
        min_y = bounds["minY"]

        pts_svg = []
        for (x, y) in pts_lae:
            sx = round((x - min_x) + 0.5)
            sy = round((y - min_y) + 0.5)
            pts_svg.append((sx, sy))

        if len(pts_svg) == 1:
            # Single point: draw a circle
            sx, sy = pts_svg[0]
            SubElement(
                svg,
                "circle",
                {
                    "cx": str(sx),
                    "cy": str(sy),
                    "r": "1",  # 1 unit radius
                    "fill": "black",
                },
            )
        else:
            # Draw Bresenham path between each pair
            for i in range(len(pts_svg) - 1):
                self._bresenham_line(pts_svg[i], pts_svg[i + 1], svg)

            # Draw circles at each point
            for (sx, sy) in pts_svg:
                SubElement(
                    svg,
                    "circle",
                    {
                        "cx": str(sx),
                        "cy": str(sy),
                        "r": "1",
                        "fill": "black",
                    },
                )

        tree = ElementTree(svg)
        tree.write(path, encoding="utf-8", xml_declaration=True)
