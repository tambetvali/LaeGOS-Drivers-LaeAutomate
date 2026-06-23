import os
import json
import csv


class LaeJSON:
    def __init__(self, filename: str, r: str, width: int, height: int):
        self.r = r
        self.filename = filename
        self.width = int(width)
        self.height = int(height)
        self.points = []  # (i, j, x_center, y_center)

    def add_point(self, i: int, j: int, x_center: float, y_center: float):
        self.points.append((int(i), int(j), float(x_center), float(y_center)))

    def save(self):
        os.makedirs(self.r, exist_ok=True)

        # JSON
        json_path = os.path.join(self.r, self.filename)
        data = {
            "R": self.r,
            "WidthSquares": self.width,
            "HeightSquares": self.height,
            "Points": [
                {
                    "i": i,
                    "j": j,
                    "x_center": x_center,
                    "y_center": y_center,
                }
                for (i, j, x_center, y_center) in self.points
            ],
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        # CSV
        base = os.path.splitext(self.filename)[0]
        csv_path = os.path.join(self.r, base + ".csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["i", "j", "x_center", "y_center"])
            for (i, j, x_center, y_center) in self.points:
                w.writerow([i, j, x_center, y_center])
