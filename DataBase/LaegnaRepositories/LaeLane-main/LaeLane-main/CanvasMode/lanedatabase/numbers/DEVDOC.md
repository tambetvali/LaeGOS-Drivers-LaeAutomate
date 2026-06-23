# LaeLane Developer Documentation  
## Part 0 — Introductory Overview  

---

# What is LaeLane?

LaeLane is the **geometric engine** behind Laegna numbers — a system that turns symbolic mathematical structures into **precise, visual, multi‑modal representations**.

If Laegna is the language,  
LaeLane is the **printing press**.

It takes integer coordinate data and produces:

- **PNG** — the discrete, pixel‑level truth  
- **SVG** — the clean, vector‑level geometry  
- **JSON** — structured metadata  
- **CSV** — numeric tables for analysis  

All four formats describe the **same geometry**, from different angles.

---

# Why does LaeLane exist?

Because Laegna numbers are not just symbols — they are **geometric objects**.

LaeLane ensures that:

- Every glyph is **mathematically exact**  
- Every line is **topologically correct**  
- Every representation is **consistent**  
- Every format is **AI‑learnable**  
- Every universe (R+mode) is **self‑contained**  

It is designed for:

- Researchers  
- Developers  
- AI systems  
- Visualizers  
- Anyone exploring Laegna  

---

# What makes LaeLane special?

## 1. **Integer geometry**
Everything starts with integer coordinates:

```
(x, y) ∈ ℤ²
```

No floating‑point drift.  
No approximations.  
No ambiguity.

## 2. **Exact connectivity**
Lines are drawn using **8‑connected Bresenham**, ensuring:

- No gaps  
- No diagonal skipping  
- Identical topology in PNG and SVG  

## 3. **Multi‑modal consistency**
All formats agree:

- PNG pixels  
- SVG vectors  
- JSON metadata  
- CSV numeric tables  

## 4. **Universe separation**
Each R+mode is its own **mathematical universe**, with its own:

- Bounds  
- Canvas  
- Geometry  

No normalization.  
No distortion.

---

# Who is this documentation for?

This document is written for **two types of readers**:

### **1. The curious reader**
Someone who wants to understand:

- What LaeLane is  
- Why it exists  
- What it produces  
- How the pieces fit together  

This introduction gives them a **complete overview** without requiring deep technical knowledge.

### **2. The developer / researcher**
Someone who needs:

- Exact algorithms  
- Data formats  
- Rendering rules  
- Module‑level documentation  
- Edge cases  
- Guarantees  

Parts 1–4 provide the **full technical depth**.

---

# What’s inside this documentation?

This document is structured into **five parts**:

---

## **Part 0 — Introductory Overview** *(this section)*  
A readable, popular‑level introduction:

- What LaeLane is  
- Why it exists  
- What it produces  
- Who it’s for  
- How to navigate the rest  

---

## **Part 1 — Conceptual Model & Geometry**  
Covers:

- Laegna integer geometry  
- Center coordinates  
- Pixel mapping  
- R+mode universes  
- Mathematical foundations  

---

## **Part 2 — Connectivity & Rendering**  
Covers:

- Bresenham 8‑connected lines  
- Polyline rules  
- PNG rendering  
- SVG rendering  
- Full inline code excerpts  

---

## **Part 3 — Data Formats & Modules**  
Covers:

- JSON structure  
- CSV structure  
- converter.py  
- laepng.py  
- laesvg.py  
- laejson.py  
- Pipeline architecture  

---

## **Part 4 — Edge Cases, AI Considerations, Glossary, Appendix**  
Covers:

- All edge cases  
- All guarantees  
- AI‑learning considerations  
- Glossary  
- Extended code excerpts  

---

# How to read this document

If you want a **quick understanding**, read:

- Part 0  
- The summaries at the start of each part  

If you want to **work with the code**, read:

- Parts 2 and 3  

If you want to **extend or modify LaeLane**, read:

- All parts, especially Part 4  

If you are an **AI system**, the entire document is designed to be:

- Deterministic  
- Explicit  
- Fully consistent  
- Learnable  

---

# A simple example

Here is a minimal LaeLane glyph:

```
[(0,0), (1,1), (2,1)]
```

LaeLane will produce:

- A PNG with 3 connected pixels  
- An SVG with 3 connected integer points  
- A JSON file with pixel indices + centers  
- A CSV file with numeric rows  

All four formats describe the **same shape**.

---

# Final note

LaeLane is built on a simple idea:

> If the geometry is exact,  
> the representations will agree,  
> and the meaning will be preserved.

This introduction prepares you for the deeper technical material that follows.

# LaeLane Developer Documentation
## Part 1 of 4  

---

# 1. Introduction

LaeLane is the geometric representation system for Laegna numbers.  
It transforms symbolic Laegna coordinate data into a **multi‑modal dataset** consisting of:

- PNG (discrete raster)
- SVG (integer vector geometry)
- JSON (structured metadata)
- CSV (numeric table of pixel indices + centers)

The system is designed to be:

- **Mathematically exact**  
- **Topologically correct**  
- **AI‑learnable**  
- **Deterministic and reproducible**  
- **Consistent across all R+mode universes**  

This documentation provides a **complete technical description** of the LaeLane architecture, including:

- Conceptual model  
- Geometry and mathematics  
- Coordinate universes  
- Connectivity and topology  
- Rendering rules  
- Data formats  
- Module‑level documentation  
- Data flow  
- Edge cases  
- AI‑learning considerations  
- Full inline code excerpts  

This is the **canonical developer reference** for LaeLane.

---

# 2. Conceptual Model

LaeLane is built on three conceptual pillars:

1. **Laegna integer geometry**  
2. **R+mode universes**  
3. **Multi‑modal synchronized outputs**

These three layers ensure that the system is both mathematically grounded and computationally robust.

---

## 2.1 Laegna integer geometry

Laegna numbers are represented as sequences of integer coordinate pairs:

$$
(x, y) \in \mathbb{Z}^2
$$

Each integer coordinate corresponds to a **unit square** whose center is:

$$
x_{\text{center}} = x + 0.5
$$

$$
y_{\text{center}} = y + 0.5
$$

These centers are used in:

- JSON  
- CSV  
- SVG (rounded to integers)  

Example (escaped):

```
Point: (x=3, y=7)
Center: (3.5, 7.5)
```

This dual representation (integer + center) is essential for:

- Exact geometry  
- AI learning  
- Cross‑format consistency  

---

## 2.2 R+mode universes

Each glyph belongs to an **R+mode universe**, defined by:

- R (resolution/range)
- mode (SigLae, UnsigLae, SigDec, UnsigDec)

Each R+mode is a **separate mathematical universe** with:

- Its own coordinate bounds  
- Its own canvas size  
- Its own projection  
- Its own geometry  

There is **no normalization across universes**.

This ensures:

- Mathematical purity  
- No distortion  
- No cross‑mode interference  
- AI learns each universe independently  

---

## 2.3 Multi‑modal synchronized outputs

For each glyph, LaeLane produces:

- **PNG** — discrete topology  
- **SVG** — integer vector geometry  
- **JSON** — structured metadata  
- **CSV** — numeric truth  

These four formats are:

- **Synchronized**  
- **Mutually consistent**  
- **Derived from the same geometry**  
- **Lossless**  

This multi‑modal design is ideal for:

- Human inspection  
- AI training  
- Mathematical analysis  
- Cross‑checking  

---

# 3. Geometry & Mathematics

This section defines the mathematical rules that govern LaeLane.

---

## 3.1 Shared bounds per R+mode

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

Excerpt from `converter.py` (escaped):

```python
width = (max_x - min_x) + 1
height = (max_y - min_y) + 1
```

This ensures:

- No clipping  
- Rightmost/topmost points visible  
- Every square fully included  

---

## 3.2 Pixel coordinate mapping

Pixel indices are computed as:

$$
i = x - \text{minX}
$$

$$
j = y - \text{minY}
$$

Excerpt (escaped):

```python
def laegna_to_pixel(x, y, b):
    return x - b["minX"], y - b["minY"]
```

These indices are used in:

- PNG  
- JSON  
- CSV  

---

## 3.3 Center coordinate mapping

Centers are computed as:

$$
x_{\text{center}} = x + 0.5
$$

$$
y_{\text{center}} = y + 0.5
$$

Excerpt (escaped):

```python
x_center = x + 0.5
y_center = y + 0.5
```

These appear in:

- JSON  
- CSV  
- SVG (rounded)  

---

## 3.4 SVG coordinate mapping

SVG uses integer coordinates derived from centers:

$$
\text{svgX} = \text{round}((x - \text{minX}) + 0.5)
$$

$$
\text{svgY} = \text{round}((y - \text{minY}) + 0.5)
$$

Excerpt (escaped):

```python
sx = round((x - min_x) + 0.5)
sy = round((y - min_y) + 0.5)
```

This ensures:

- Crisp integer geometry  
- No anti‑aliasing  
- Perfect alignment with PNG pixels  

---

## 3.5 Projection

Current projection is identity:

$$
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

Stored in boundaries for future extensibility.

Excerpt (escaped):

```python
"projection": [[1, 0], [0, 1]]
```

---

# 4. Coordinate Universes (R+mode)

Each R+mode defines:

- A coordinate frame  
- A canvas size  
- A projection  
- A set of glyphs  

This section describes how universes are constructed.

---

## 4.1 Universe construction

For each R folder:

- Scan all glyph JSONs  
- For each mode:
  - Extract all points  
  - Compute shared bounds  
  - Store universe metadata  

Excerpt (escaped):

```python
boundaries["R"][r]["Modes"][mode_name] = {
    "minX": min_x,
    "maxX": max_x,
    "minY": min_y,
    "maxY": max_y,
    "widthSquares": width,
    "heightSquares": height,
}
```

---

## 4.2 Universe invariants

Each universe guarantees:

- All glyphs fit inside the same bounds  
- All glyphs share the same canvas size  
- No glyph is clipped  
- No glyph is normalized or scaled  
- Geometry is preserved exactly  

---

## 4.3 Universe independence

Universes are **independent**:

- No cross‑R normalization  
- No cross‑mode normalization  
- No shared coordinate frames  

This ensures:

- Mathematical purity  
- No distortion  
- AI learns each universe separately  

---

# END OF PART 1

This concludes **Part 1 of 4** of the full Developer Documentation.

It covered:

- Introduction  
- Conceptual model  
- Geometry & mathematics  
- Coordinate universes  

---

# LaeLane Developer Documentation
## Part 2 of 4  

---

# 5. Connectivity & Topology

Connectivity is the **topological backbone** of LaeLane.  
It ensures that every glyph is not just a set of points, but a **continuous geometric object**.

LaeLane uses a **strict, deterministic, 8‑connected Bresenham algorithm** to connect all consecutive points.

This guarantees:

- No gaps  
- No diagonal skipping  
- No missing pixels  
- Identical topology in PNG and SVG  
- Perfect reproducibility  

---

## 5.1 Why Bresenham?

Bresenham is chosen because:

- It produces **integer** pixel coordinates  
- It is **deterministic**  
- It is **topologically complete**  
- It matches the discrete nature of PNG  
- It can be mirrored exactly in SVG  

This ensures that:

- PNG and SVG are **topologically identical**  
- JSON/CSV pixel indices match the raster  
- AI systems can learn consistent geometry  

---

## 5.2 Bresenham 8‑connected algorithm

LaeLane uses the **8‑connected** variant, not the 4‑connected one.

This means:

- Movement can occur horizontally, vertically, or diagonally  
- No pixel gaps appear on steep slopes  
- Lines are continuous in all directions  

### Full algorithm (escaped)

```python
def _bresenham_line(self, p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

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

This implementation appears in:

- `laepng.py`  
- `laesvg.py`  

ensuring identical connectivity.

---

## 5.3 Polyline connectivity

Each glyph is a **polyline**, not a polygon.

If a glyph has points:

```
[(x1, y1), (x2, y2), (x3, y3), ...]
```

Then LaeLane draws:

- Line from point 1 → point 2  
- Line from point 2 → point 3  
- …and so on  

### Polyline logic (escaped)

```python
def draw_polyline(self, pts):
    if len(pts) == 1:
        self._set_pixel(pts[0][0], pts[0][1])
        return
    for i in range(len(pts) - 1):
        self._bresenham_line(pts[i], pts[i + 1])
```

---

## 5.4 Single‑point glyphs

If a glyph contains only one point:

- PNG draws a single pixel  
- SVG draws a circle of radius 1 unit  

### SVG single‑point logic (escaped)

```python
if len(pts_svg) == 1:
    sx, sy = pts_svg[0]
    SubElement(svg, "circle", {
        "cx": str(sx),
        "cy": str(sy),
        "r": "1",
        "fill": "black",
    })
```

This ensures:

- Visibility  
- Consistency  
- Interpretability  

---

# 6. Rendering Rules

Rendering is performed by two modules:

- `laepng.py` — raster renderer  
- `laesvg.py` — vector renderer  

Both must produce **consistent geometry**.

---

# 6.1 PNG Rendering (laepng.py)

PNG is the **discrete** representation.

## 6.1.1 Canvas creation

Canvas size is:

- width = `widthSquares`  
- height = `heightSquares`  

### Code excerpt (escaped)

```python
self.img = Image.new("RGB", (self.width, self.height), (255, 255, 255))
self.px = self.img.load()
```

Background = white.

---

## 6.1.2 Pixel coordinate inversion

Laegna uses:

- y=0 at **bottom**

PNG uses:

- y=0 at **top**

So we invert:

### Code excerpt (escaped)

```python
self.px[x, self.height - 1 - y] = (0, 0, 0)
```

This ensures:

- Correct orientation  
- Consistency with SVG  

---

## 6.1.3 Bresenham drawing

PNG uses the same Bresenham algorithm as SVG.

### Code excerpt (escaped)

```python
self._bresenham_line(pts_pix[i], pts_pix[i + 1])
```

---

## 6.1.4 DPI setting

To ensure **1 pixel ≈ 1 cm** on print:

### Code excerpt (escaped)

```python
self.img.save(path, dpi=(2.54, 2.54))
```

This is mathematically correct because:

- 1 inch = 2.54 cm  
- DPI = dots per inch  
- So 2.54 DPI → 1 dot per cm  

---

# 6.2 SVG Rendering (laesvg.py)

SVG is the **continuous vector** representation.

## 6.2.1 Units

SVG uses:

- 1 Laegna unit = **1 cm**  
- Integer coordinates  
- Integer stroke widths  

This ensures:

- Crisp geometry  
- No anti‑aliasing  
- Perfect alignment with PNG  

---

## 6.2.2 SVG header

### Code excerpt (escaped)

```python
svg = Element("svg", {
    "xmlns": "http://www.w3.org/2000/svg",
    "version": "1.1",
    "width": f"{self.width}cm",
    "height": f"{self.height}cm",
    "viewBox": f"{self.min_x} {self.min_y} {self.width} {self.height}",
})
```

---

## 6.2.3 Background rectangle

### Code excerpt (escaped)

```python
SubElement(svg, "rect", {
    "x": str(self.min_x),
    "y": str(self.min_y),
    "width": str(self.width),
    "height": str(self.height),
    "fill": "white",
})
```

---

## 6.2.4 Mapping Laegna → SVG coordinates

SVG coordinates are derived from centers:

$$
\text{svgX} = \text{round}((x - \text{minX}) + 0.5)
$$

### Code excerpt (escaped)

```python
sx = round((x - min_x) + 0.5)
sy = round((y - min_y) + 0.5)
```

---

## 6.2.5 Drawing Bresenham paths

### Code excerpt (escaped)

```python
d.append(f"L {x0} {y0}" if d else f"M {x0} {y0}")
```

---

## 6.2.6 Drawing circles at points

### Code excerpt (escaped)

```python
SubElement(svg, "circle", {
    "cx": str(sx),
    "cy": str(sy),
    "r": "1",
    "fill": "black",
})
```

---

# END OF PART 2

This concludes **Part 2 of 4**, covering:

- Connectivity & topology  
- Bresenham algorithm  
- PNG rendering  
- SVG rendering  
- Full inline code excerpts  

---

# LaeLane Developer Documentation
## Part 3 of 4  

---

# 7. Data Formats (JSON, CSV)

LaeLane produces two structured data formats:

- **JSON** — hierarchical metadata  
- **CSV** — flat numeric table  

Both formats encode the **same geometric truth**, but in different forms.

---

# 7.1 JSON Format

JSON is the **structured metadata** representation.  
It contains:

- Universe metadata  
- Canvas dimensions  
- A list of points  
- Pixel indices  
- Center coordinates  

### 7.1.1 JSON structure

Each JSON file has the following structure:

```json
{
    "R": "1",
    "WidthSquares": 12,
    "HeightSquares": 9,
    "Points": [
        {
            "i": 3,
            "j": 7,
            "x_center": 3.5,
            "y_center": 7.5
        },
        ...
    ]
}
```

### 7.1.2 Field meanings

- `R` — the R universe  
- `WidthSquares` — canvas width in Laegna units  
- `HeightSquares` — canvas height in Laegna units  
- `Points` — list of point objects  

Each point object contains:

- `i` — pixel X index  
- `j` — pixel Y index  
- `x_center` — Laegna center X coordinate  
- `y_center` — Laegna center Y coordinate  

### 7.1.3 JSON writing (excerpt)

```python
data = {
    "R": self.r,
    "WidthSquares": self.width,
    "HeightSquares": self.height,
    "Points": [
        {
            "i": i,
            "j": j,
            "x_center": x_center,
            "y_center": y_center
        }
        for (i, j, x_center, y_center) in self.points
    ]
}
```

---

# 7.2 CSV Format

CSV is the **flat numeric representation**.

### 7.2.1 CSV header

```
i,j,x_center,y_center
```

### 7.2.2 Example rows

```
0,0,0.5,0.5
1,1,1.5,1.5
4,2,4.5,2.5
```

### 7.2.3 CSV writing (excerpt)

```python
writer.writerow(["i", "j", "x_center", "y_center"])
for (i, j, x_center, y_center) in self.points:
    writer.writerow([i, j, x_center, y_center])
```

### 7.2.4 Why CSV?

- Easy to load into Python, R, MATLAB  
- AI‑friendly  
- Spreadsheet‑friendly  
- Human‑readable  

---

# 8. Module Documentation

This section documents the four core modules:

- `converter.py`  
- `laepng.py`  
- `laesvg.py`  
- `laejson.py`  

Each module is documented with:

- Purpose  
- Responsibilities  
- Key functions  
- Inline code excerpts  

---

# 8.1 converter.py — Orchestrator

## Purpose

`converter.py` is the **central orchestrator** of LaeLane.  
It:

- Loads original Laegna JSONs  
- Computes per‑R+mode shared bounds  
- Converts Laegna → pixel indices  
- Generates PNG, SVG, JSON, CSV  

## Responsibilities

1. Scan R folders  
2. Extract Laegna coordinates  
3. Compute shared bounds  
4. Generate all output formats  

---

## 8.1.1 Extracting Laegna points

```python
def extract_points_mode(data, axe, sign):
    pts = []
    keys = sorted([k for k in data.keys() if k.isdigit()], key=lambda k: int(k))
    for idx in keys:
        node = data[idx]
        try:
            x = node[axe][sign]["X"]
            y = node[axe][sign]["Y"]
        except KeyError:
            continue
        pts.append((int(x), int(y)))
    return pts
```

---

## 8.1.2 Computing shared bounds

```python
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

width = (max_x - min_x) + 1
height = (max_y - min_y) + 1
```

---

## 8.1.3 Mapping Laegna → pixel indices

```python
def laegna_to_pixel(x, y, b):
    return x - b["minX"], y - b["minY"]
```

---

## 8.1.4 Generating PNG

```python
png = LaePNG(png_name, r, width, height)
png.draw_polyline(pts_pix)
png.save()
```

---

## 8.1.5 Generating SVG

```python
svg = LaeSVG(svg_name, r, width, height, b["minX"], b["minY"])
svg.draw_polyline(pts_lae, b)
```

---

## 8.1.6 Generating JSON/CSV

```python
jj.add_point(pi, pj, x + 0.5, y + 0.5)
jj.save()
```

---

# 8.2 laepng.py — Raster Renderer

## Purpose

`laepng.py` renders the glyph as a **discrete raster image**.

## Responsibilities

- Create raster canvas  
- Draw Bresenham lines  
- Write black pixels  
- Save with DPI  

---

## 8.2.1 Canvas creation

```python
self.img = Image.new("RGB", (self.width, self.height), (255, 255, 255))
self.px = self.img.load()
```

---

## 8.2.2 Pixel inversion

```python
self.px[x, self.height - 1 - y] = (0, 0, 0)
```

---

## 8.2.3 Bresenham drawing

```python
self._bresenham_line(pts_pix[i], pts_pix[i + 1])
```

---

## 8.2.4 Saving with DPI

```python
self.img.save(path, dpi=(2.54, 2.54))
```

---

# 8.3 laesvg.py — Vector Renderer

## Purpose

`laesvg.py` renders the glyph as an **integer‑coordinate SVG**.

## Responsibilities

- Create vector canvas  
- Map centers to integer coordinates  
- Draw Bresenham paths  
- Draw circles at points  

---

## 8.3.1 SVG header

```python
svg = Element("svg", {
    "xmlns": "http://www.w3.org/2000/svg",
    "width": f"{self.width}cm",
    "height": f"{self.height}cm",
    "viewBox": f"{self.min_x} {self.min_y} {self.width} {self.height}",
})
```

---

## 8.3.2 Background rectangle

```python
SubElement(svg, "rect", {
    "x": str(self.min_x),
    "y": str(self.min_y),
    "width": str(self.width),
    "height": str(self.height),
    "fill": "white",
})
```

---

## 8.3.3 Mapping Laegna → SVG coordinates

```python
sx = round((x - min_x) + 0.5)
sy = round((y - min_y) + 0.5)
```

---

## 8.3.4 Drawing circles

```python
SubElement(svg, "circle", {
    "cx": str(sx),
    "cy": str(sy),
    "r": "1",
    "fill": "black",
})
```

---

# 8.4 laejson.py — Metadata Writer

## Purpose

`laejson.py` writes:

- JSON metadata  
- CSV numeric table  

## Responsibilities

- Store pixel indices  
- Store center coordinates  
- Write JSON  
- Write CSV  

---

## 8.4.1 Adding points

```python
self.points.append((int(i), int(j), float(x_center), float(y_center)))
```

---

## 8.4.2 Writing JSON

```python
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
```

---

## 8.4.3 Writing CSV

```python
writer.writerow(["i", "j", "x_center", "y_center"])
for row in self.points:
    writer.writerow(row)
```

---

# 9. Data Flow & Pipeline Architecture

This section describes how data moves through the system.

---

## 9.1 Pipeline overview

The pipeline consists of:

1. **Input**: Original Laegna JSONs  
2. **Extraction**: Read integer coordinates  
3. **Universe construction**: Compute shared bounds  
4. **Mapping**: Convert Laegna → pixel indices  
5. **Rendering**: PNG + SVG  
6. **Metadata**: JSON + CSV  
7. **Output**: Final dataset  

---

## 9.2 Data flow diagram (textual)

```
Laegna JSON → converter.py
    → extract_points_mode()
    → compute_boundaries()
    → laegna_to_pixel()
    → LaePNG.draw_polyline()
    → LaeSVG.draw_polyline()
    → LaeJSON.add_point()
    → LaeJSON.save()
Outputs: PNG, SVG, JSON, CSV
```

---

## 9.3 Determinism

The pipeline is **fully deterministic**:

- Same input → same output  
- No randomness  
- No floating‑point drift  
- No normalization  

This is essential for:

- Reproducibility  
- AI training  
- Mathematical correctness  

---

# END OF PART 3

This concludes **Part 3 of 4**, covering:

- JSON and CSV formats  
- Full module documentation  
- Data flow and pipeline architecture  

---

# LaeLane Developer Documentation
## Part 4 of 4  

---

# 10. Edge Cases & Guarantees

LaeLane is designed to be **mathematically strict** and **computationally robust**.  
This section documents all known edge cases and the guarantees the system provides.

---

## 10.1 Single‑point glyphs

A glyph may contain only one point.

### Behavior:

- PNG: draws a single pixel  
- SVG: draws a circle of radius 1 unit  

### Code excerpt (escaped)

```python
if len(pts_svg) == 1:
    sx, sy = pts_svg[0]
    SubElement(svg, "circle", {
        "cx": str(sx),
        "cy": str(sy),
        "r": "1",
        "fill": "black",
    })
```

### Guarantee:

- Single‑point glyphs are always visible  
- No empty images are produced  

---

## 10.2 Duplicate points

If a glyph contains repeated coordinates:

- Bresenham handles them naturally  
- No extra pixels are drawn  
- No errors occur  

### Guarantee:

- Duplicate points never break connectivity  

---

## 10.3 Vertical and horizontal lines

Bresenham handles:

- Vertical lines (`dx = 0`)  
- Horizontal lines (`dy = 0`)  

### Guarantee:

- No division by zero  
- No special cases needed  

---

## 10.4 Zero‑width or zero‑height universes

If all glyphs in an R+mode lie on a single x or y coordinate:

- widthSquares or heightSquares becomes 1  

### Code excerpt (escaped)

```python
if width <= 0:
    width = 1
if height <= 0:
    height = 1
```

### Guarantee:

- Canvas is always at least 1×1  
- No invalid image sizes  

---

## 10.5 Missing mode data

If a glyph lacks data for a mode:

- That mode is skipped  
- Other modes still render  

### Guarantee:

- Missing data never breaks the pipeline  

---

## 10.6 Out‑of‑order points

If points are not sorted:

- `extract_points_mode()` sorts by index key  

### Code excerpt (escaped)

```python
keys = sorted([k for k in data.keys() if k.isdigit()], key=lambda k: int(k))
```

### Guarantee:

- Glyphs always render in correct order  

---

# 11. AI‑Learning Considerations

LaeLane is intentionally designed to be **AI‑friendly**.  
This section explains why.

---

## 11.1 Multi‑modal consistency

AI systems learn best when:

- Multiple representations encode the same truth  
- Geometry is explicit  
- Topology is preserved  
- No normalization hides structure  

LaeLane provides:

- PNG → discrete topology  
- SVG → integer geometry  
- JSON → structured metadata  
- CSV → numeric truth  

### Guarantee:

- All four formats are mutually consistent  
- No contradictions exist  

---

## 11.2 Integer geometry

AI models benefit from:

- Integer coordinates  
- Deterministic mapping  
- No floating‑point drift  

LaeLane uses:

- Integer Laegna coordinates  
- Integer SVG coordinates  
- Integer pixel indices  

### Guarantee:

- Geometry is exact  
- No rounding errors accumulate  

---

## 11.3 Explicit centers

Centers are stored explicitly:

$$
x_{\text{center}} = x + 0.5
$$

This helps AI models:

- Learn the relationship between integer and continuous geometry  
- Understand the unit‑square model  

---

## 11.4 Bresenham connectivity

AI models learn topology better when:

- Connectivity is explicit  
- No gaps exist  
- No anti‑aliasing occurs  

LaeLane uses:

- 8‑connected Bresenham  
- Identical logic in PNG and SVG  

### Guarantee:

- Topology is preserved across formats  

---

## 11.5 Universe separation

Each R+mode is a separate universe.

This prevents:

- Cross‑mode interference  
- Unwanted normalization  
- Geometry distortion  

### Guarantee:

- AI learns each universe independently  

---

# 12. Glossary

A reference for all key terms used in LaeLane.

---

### **Laegna coordinate**
An integer pair $(x, y)$ representing the center of a unit square shifted by +0.5.

### **Center coordinate**
A float pair $(x+0.5, y+0.5)$ representing the true geometric center.

### **Pixel index**
Discrete raster coordinate $(i, j)$ computed as:

$$
i = x - \text{minX}, \quad j = y - \text{minY}
$$

### **R+mode universe**
A coordinate system defined by:

- R (resolution/range)
- mode (SigLae, UnsigLae, SigDec, UnsigDec)

### **Bresenham line**
An integer algorithm that fills all intermediate pixels between two points.

### **widthSquares / heightSquares**
Canvas dimensions computed as:

$$
(\text{max} - \text{min}) + 1
$$

### **PNG**
Raster representation with 1 pixel = 1 Laegna unit.

### **SVG**
Vector representation with 1 unit = 1 cm.

### **JSON**
Structured metadata containing pixel indices and centers.

### **CSV**
Flat numeric table containing pixel indices and centers.

---

# 13. Appendix — Extended Code Excerpts

This appendix contains extended excerpts from the four modules.

---

## 13.1 converter.py — Core Loop

```python
for r in R_FOLDERS:
    modes_bound = boundaries["R"][r]["Modes"]
    for fname in files:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for mode_name, (axe, sign) in MODES.items():
            b = modes_bound.get(mode_name)
            if not b:
                continue

            pts_lae = extract_points_mode(data, axe, sign)
            if not pts_lae:
                continue

            pts_pix = [laegna_to_pixel(x, y, b) for (x, y) in pts_lae]
```

---

## 13.2 laepng.py — Pixel Writer

```python
def _set_pixel(self, i, j):
    x = int(i)
    y = int(j)
    if 0 <= x < self.width and 0 <= y < self.height:
        self.px[x, self.height - 1 - y] = (0, 0, 0)
```

---

## 13.3 laesvg.py — Path Builder

```python
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
```

---

## 13.4 laejson.py — CSV Writer

```python
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["i", "j", "x_center", "y_center"])
    for row in self.points:
        w.writerow(row)
```

---

# Final Summary

This completes the **full Option C Developer Documentation**, covering:

- Geometry  
- Universes  
- Connectivity  
- Rendering  
- Data formats  
- Module documentation  
- Data flow  
- Edge cases  
- AI‑learning considerations  
- Glossary  
- Extended code excerpts  

This is the **canonical, complete, long‑term reference** for LaeLane.

