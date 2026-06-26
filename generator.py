from utilities import *
import json
import os

def generate(Rs, folder):
    global R, laeaxes, laeranges

    laeaxes, laeranges = cleanlanecache()

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
            datacanvas["R"][r][laen.Lae4()] = laen.generatePointsCanvas()

    data["axes"] = laeaxes.axes

    datacanvas["ranges"] = {}

    for r in laeranges.ranges:
        datacanvas["ranges"][r] = laeranges.simp(r)

    if not os.path.exists(folder):
        os.mkdir(folder)

    with open(folder + "/lanes.json", "w") as f:
        json.dump(data, f, indent=4)  # indent for pretty formatting

    with open(folder + "/canvas.json", "w") as f:
        json.dump(datacanvas, f, indent=4)  # indent for pretty formatting

Rs = [0.5, 1, 2, 3, 4]
generate(Rs, "gosdb")

Rs = [0.5, 1, 2, 3]
generate(Rs, "gosdb-small")

Rs = [0.5, 1, 2]
generate(Rs, "gosdb-mini")

