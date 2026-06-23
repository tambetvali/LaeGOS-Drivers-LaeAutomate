import os
from PIL import Image


class LaePNG:
    def __init__(self, filename: str, r: str, width: int, height: int):
        self.r = r
        self.filename = filename
        self.width = int(width)      # pixels, 1 px = 1 unit
        self.height = int(height)

        self.img = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.px = self.img.load()

    def _set_pixel(self, i: int, j: int):
        x = int(i)
        y = int(j)
        if 0 <= x < self.width and 0 <= y < self.height:
            # y=0 at bottom in Laegna; invert for image
            self.px[x, self.height - 1 - y] = (0, 0, 0)

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

    def draw_polyline(self, pts_pix):
        if not pts_pix:
            return
        if len(pts_pix) == 1:
            self._set_pixel(pts_pix[0][0], pts_pix[0][1])
            return
        for i in range(len(pts_pix) - 1):
            self._bresenham_line(pts_pix[i], pts_pix[i + 1])

    def save(self):
        os.makedirs(self.r, exist_ok=True)
        path = os.path.join(self.r, self.filename)
        # 1 px ≈ 1 cm → 2.54 dpi
        self.img.save(path, dpi=(2.54, 2.54))
