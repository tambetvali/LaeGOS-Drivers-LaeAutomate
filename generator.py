from utilities import *
import json
import os

def generate(Rs, folder, flipback = False):
    global R, laeaxes, laeranges

    laeaxes, laeranges = cleanlanecache()

    data = {
        "format": ("SC5N", 0, "0.8", "Data flip."),
        "axes": {},
        "R": {}
    }

    datacanvas = {
        "format": ("SC5N", 0, "0.8", "Canvas flip."),
        "ranges": {},
        "R": {}
    }

    data_unflip = {
        "format": ("SC5N", 0, "0.8", "Data unflip."),
        "axes": {},
        "R": {}
    }

    datacanvas_unflip = {
        "format": ("SC5N", 0, "0.8", "Canvas unflip."),
        "ranges": {},
        "R": {}
    }

    for r in Rs:
        data["R"][r] = {}
        datacanvas["R"][r] = {}
        data_unflip["R"][r] = {}
        datacanvas_unflip["R"][r] = {}
        for laen in R(r):
            data["R"][r][laen.Lae4()] = laen.generatePoints()
            datacanvas["R"][r][laen.Lae4()] = laen.generatePointsCanvas()
            data_unflip["R"][r][laen.Lae4()] = laen.generatePoints(unflip=True)
            datacanvas_unflip["R"][r][laen.Lae4()] = laen.generatePointsCanvas(unflip=True)

    data["axes"] = laeaxes.axes
    data_unflip["axes"] = laeaxes.axes

    datacanvas["ranges"] = {}
    datacanvas_unflip["ranges"] = {}

    for r in laeranges.ranges:
        datacanvas["ranges"][r] = laeranges.simp(r)
        datacanvas_unflip["ranges"][r] = laeranges.simp(r)

    if not os.path.exists(folder):
        os.mkdir(folder)

    with open(folder + "/lanes.json", "w") as f:
        json.dump(data, f, indent=4)  # indent for pretty formatting

    with open(folder + "/canvas.json", "w") as f:
        json.dump(datacanvas, f, indent=4)  # indent for pretty formatting

    with open(folder + "/lanes_unflip.json", "w") as f:
        json.dump(data_unflip, f, indent=4)  # indent for pretty formatting

    with open(folder + "/canvas_unflip.json", "w") as f:
        json.dump(datacanvas_unflip, f, indent=4)  # indent for pretty formatting

Rs = [0.5, 1, 2, 3, 4]
generate(Rs, "gosdb")

Rs = [0.5, 1, 2, 3]
generate(Rs, "gosdb-small")

Rs = [0.5, 1, 2]
generate(Rs, "gosdb-mini")

