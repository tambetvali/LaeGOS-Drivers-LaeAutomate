# LaeLane — Compact Technical Specification

This document defines the **complete minimal specification** of the LaeLane generation system.  
It describes the geometry, coordinate rules, connectivity, rendering, and the purpose of the four generator files:

- `converter.py`
- `laepng.py`
- `laesvg.py`
- `laejson.py`

The goal is to ensure that LaeLane glyphs are **mathematically exact**, **topologically correct**, and **AI‑learnable**.

---

# 1. Geometry and Coordinate System

## 1.1 Laegna integer coordinates

Each glyph consists of ordered integer coordinate pairs:

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

---

## 1.2 Per‑R+mode shared bounds

Each R+mode (e.g. `R=1`, `SigLae`) defines a **separate coordinate universe**.

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
- Rightmost/topmost points are visible  
- Every square is fully included  

---

## 1.3 Pixel coordinates

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

---

# 2. Connectivity Rules

## 2.1 Bresenham 8‑connected lines

Between each consecutive pair of points:

- Use **8‑connected Bresenham**
- Fill **every intermediate pixel**
- No diagonal skipping
- No shortcuts
- No holes

This ensures **topological correctness** in both PNG and SVG.

Internal algorithm (escaped):

```python
# Bresenham 8-connected line (conceptual)
while True:
    set_pixel(x0, y0)
    if (x0, y0) == (x1, y1):
        break
    e2 = 2 * err
    if e2 > -dy:
        err -= dy
        x0 += sx
    if e2 < dx:
        err += dx
        y0 += sy
```

---

# 3. Rendering Specifications

# 3.1 PNG (laepng.py)

- 1 pixel = 1 Laegna unit  
- Background = white  
- Foreground = black  
- Bresenham lines fill all intermediate pixels  
- y‑axis inverted so Laegna `y=0` is bottom  
- DPI = 2.54 → 1 pixel ≈ 1 cm  

Example pixel write (escaped):

```python
self.px[x, self.height - 1 - y] = (0, 0, 0)
```

---

# 3.2 SVG (laesvg.py)

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

- Bresenham lines drawn using integer coordinates  
- Circles drawn at each point  

Example mapping (escaped):

```python
sx = round((x - min_x) + 0.5)
sy = round((y - min_y) + 0.5)
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

# 3.4 CSV Columns (escaped)

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

---

# 4. File Responsibilities

## 4.1 converter.py

- Scans R folders  
- Extracts Laegna coordinates  
- Computes per‑R+mode bounds  
- Converts Laegna → pixel indices  
- Generates PNG, SVG, JSON, CSV  

Internal extraction example (escaped):

```python
x = node[axe][sign]["X"]
y = node[axe][sign]["Y"]
```

---

## 4.2 laepng.py

- Creates raster canvas  
- Draws Bresenham lines  
- Writes black pixels  
- Saves with DPI = 2.54  

---

## 4.3 laesvg.py

- Creates vector canvas  
- Maps centers to integer coordinates  
- Draws Bresenham paths  
- Draws circles at points  

---

## 4.4 laejson.py

- Writes JSON metadata  
- Writes CSV with pixel indices + centers  

CSV writer example (escaped):

```python
writer.writerow([i, j, x_center, y_center])
```

---

# 5. Summary

This specification defines:

- The Laegna coordinate system  
- Per‑R+mode universes  
- Pixel mapping rules  
- Bresenham connectivity  
- Rendering rules for PNG and SVG  
- Metadata formats (JSON, CSV)  
- Responsibilities of each generator file  

It is the **minimal complete reference** for the LaeLane system.
