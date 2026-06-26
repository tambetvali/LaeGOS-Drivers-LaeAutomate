from utilities import *
import json
import os

Rs = [0.5, 1, 2, 3, 4]

data = {
    "axes": {},
    "R": {}
}

datacanvas = {
    "ranges": {},
    "R": {}
}

for r in Rs:
    data["R"][r] = {}
    datacanvas["R"][r] = {}
    for laen in R(r):
        data["R"][r][laen.Lae4()] = laen.generatePoints()

data["axes"] = laeaxes.axes
datacanvas["ranges"] = laeranges.ranges

if not os.path.exists("lanedatabase"):
    os.mkdir("lanedatabase")

with open("lanedatabase/lanes.json", "w") as f:
    json.dump(data, f, indent=4)  # indent for pretty formatting

with open("lanedatabase/canvas.json", "w") as f:
    json.dump(datacanvas, f, indent=4)  # indent for pretty formatting

