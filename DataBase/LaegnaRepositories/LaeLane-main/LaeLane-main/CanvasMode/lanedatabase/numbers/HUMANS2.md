# LaeLane Technical Whitepaper

## Abstract

LaeLane is a geometric representation system for Laegna numbers.  
It produces mathematically exact, topologically complete, and AI‑learnable glyphs across four synchronized formats:

- PNG (discrete raster)
- SVG (integer vector geometry)
- JSON (structured metadata)
- CSV (numeric table of pixel indices + centers)

This document defines the **complete technical specification** of the LaeLane generation architecture, including:

- Geometry  
- Coordinate systems  
- Connectivity rules  
- Rendering rules  
- Data formats  
- Algorithmic details  
- Full inline code excerpts (escaped)  

It is the canonical reference for developers, researchers, and AI systems interacting with LaeLane.

---

# 1. Mathematical Foundations

## 1.1 Laegna integer geometry

Each glyph is defined by an ordered list of integer coordinate pairs:

$$
(x, y) \in \mathbb{Z}^2
$$

These represent **unit squares** whose centers are:

$$
x_{\text{center}} = x + 0.5
$$

$$
y_{\text{center}} = y + 0.5
$$

These center coordinates appear in JSON and CSV.

Example (escaped):

```
Point: (x=3, y=7)
Center: (3.5, 7.5)
```

---

## 1.2 Per‑R+mode universes

Each R+mode (e.g. `R=1`, `SigLae`) defines a **separate coordinate universe**.

Within each universe:

- All glyphs share the same bounds  
- All glyphs share the same canvas size  
- All coordinates are comparable  
- No normalization occurs across universes  

This is essential for:

- Mathematical consistency  
- AI learning  
- Visual comparability  

---

## 1.3 Shared bounds

For each R+mode:

- Collect all points from all glyphs  
- Compute:

$$
\text{minX},\ \text{maxX},\ \text{minY},\ \text{maxY}
$$

Canvas size must include **all squares**, so:

$$
\text{widthSquares} = (\text{maxX} - \text{minX}) + 1
$$

$$
\text{heightSquares} = (\text{maxY} - \text{minY}) + 1
$$

This ensures:

- No clipping  
- Rightmost/topmost points visible  
- Every square fully included  

Excerpt from `converter.py` (escaped):

```python
width = (max_x - min_x) + 1
height = (max_y - min_y) + 1
```

---

## 1.4 Pixel coordinates

Pixel indices are computed as:

$$
i = x - \text{minX}
$$

$$
j = y - \text{minY}
$$

These are integers in:

- $0 \le i < \text{widthSquares}$
- $0 \le j < \text{heightSquares}$

Excerpt (escaped):

```python
def laegna_to_pixel(x, y, b):
    return x - b["minX"], y - b["minY"]
```

---

# 2. Connectivity Rules

## 2.1 Bresenham 8‑connected lines

Between each consecutive pair of points:

- Use **8‑connected Bresenham**  
- Fill **every intermediate pixel**  
- No diagonal skipping  
- No shortcuts  
- No holes  

This ensures **topological correctness**.

Excerpt from `laepng.py` (escaped):

```python
while True:
    self._set_pixel(x0, y0)
    if x0 == x1 and y0 == y1:
        break
    e2 = 2 * err
    if e2 > -dy:
        err -= dy
        x0 += sx
    if e2 < dx:
        err += dx
        y0 += sy
```

The same algorithm is used in SVG.

---

# 3. Rendering Specifications

# 3.1 PNG (laepng.py)

### Rules

- 1 pixel = 1 Laegna unit  
- Background = white  
- Foreground = black  
- Bresenham lines fill all intermediate pixels  
- y‑axis inverted so Laegna `y=0` is bottom  
- DPI = 2.54 → 1 pixel ≈ 1 cm  

### Pixel inversion

Excerpt (escaped):

```python
self.px[x, self.height - 1 - y] = (0, 0, 0)
```

### Saving with DPI

```python
self.img.save(path, dpi=(2.54, 2.54))
```

---

# 3.2 SVG (laesvg.py)

### Rules

- 1 Laegna unit = 1 cm  
- `width="Wcm"` and `height="Hcm"`  
- `viewBox="minX minY widthSquares heightSquares"`  
- Coordinates are **integers**  
- Centers mapped as:

$$
\text{svgX} = \text{round}((x - \text{minX}) + 0.5)
$$

$$
\text{svgY} = \text{round}((y - \text{minY}) + 0.5)
$$

### Mapping excerpt

```python
sx = round((x - min_x) + 0.5)
sy = round((y - min_y) + 0.5)
```

### Drawing circles

```python
SubElement(svg, "circle", {
    "cx": str(sx),
    "cy": str(sy),
    "r": "1",
    "fill": "black",
})
```

---

# 3.3 JSON (laejson.py)

JSON stores:

- R  
- widthSquares  
- heightSquares  
- List of points with:
  - pixel indices `(i, j)`
  - center coordinates `(x_center, y_center)`

Example JSON entry (escaped):

```json
{
  "i": 3,
  "j": 7,
  "x_center": 3.5,
  "y_center": 7.5
}
```

---

# 3.4 CSV Format

CSV header:

```
i,j,x_center,y_center
```

Example rows:

```
0,0,0.5,0.5
1,1,1.5,1.5
4,2,4.5,2.5
```

Meaning:

- `i, j` → discrete pixel indices  
- `x_center, y_center` → true Laegna geometry  

CSV writer excerpt:

```python
writer.writerow([i, j, x_center, y_center])
```

---

# 4. File Responsibilities (with inline excerpts)

## 4.1 converter.py — Orchestrator

Responsibilities:

- Scan R folders  
- Extract Laegna coordinates  
- Compute per‑R+mode bounds  
- Convert Laegna → pixel indices  
- Generate PNG, SVG, JSON, CSV  

### Extracting points

```python
x = node[axe][sign]["X"]
y = node[axe][sign]["Y"]
```

### Generating PNG

```python
png = LaePNG(png_name, r, width, height)
png.draw_polyline(pts_pix)
png.save()
```

### Generating SVG

```python
svg = LaeSVG(svg_name, r, width, height, b["minX"], b["minY"])
svg.draw_polyline(pts_lae, b)
```

### Generating JSON/CSV

```python
jj.add_point(pi, pj, x + 0.5, y + 0.5)
jj.save()
```

---

## 4.2 laepng.py — Raster Renderer

Responsibilities:

- Create raster canvas  
- Draw Bresenham lines  
- Write black pixels  
- Save with DPI  

### Canvas creation

```python
self.img = Image.new("RGB", (self.width, self.height), (255, 255, 255))
```

---

## 4.3 laesvg.py — Vector Renderer

Responsibilities:

- Create vector canvas  
- Map centers to integer coordinates  
- Draw Bresenham paths  
- Draw circles at points  

### SVG header

```python
svg = Element("svg", {
    "xmlns": "http://www.w3.org/2000/svg",
    "width": f"{self.width}cm",
    "height": f"{self.height}cm",
    "viewBox": f"{self.min_x} {self.min_y} {self.width} {self.height}",
})
```

---

## 4.4 laejson.py — Metadata Writer

Responsibilities:

- Write JSON metadata  
- Write CSV with pixel indices + centers  

### JSON structure

```python
data = {
    "R": self.r,
    "WidthSquares": self.width,
    "HeightSquares": self.height,
    "Points": [...]
}
```

---

# 5. Summary

This whitepaper defines:

- The Laegna coordinate system  
- Per‑R+mode universes  
- Pixel mapping rules  
- Bresenham connectivity  
- Rendering rules for PNG and SVG  
- Metadata formats (JSON, CSV)  
- Responsibilities of each generator file  
- Inline code excerpts for clarity  

It is the **complete technical reference** for LaeLane.

