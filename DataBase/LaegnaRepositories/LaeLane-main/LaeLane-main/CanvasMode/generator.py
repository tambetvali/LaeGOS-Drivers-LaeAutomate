from utilities import *
import json
import os

Rs = [0.5, 1, 2, 3, 4]

data = {
    "axes": {},
    "R": {}
}

for r in Rs:
    data["R"][r] = {}
    for laen in R(r):
        data["R"][r][laen.Lae4()] = laen.generatePoints()

data["axes"] = laeaxes.axes

if not os.path.exists("lanedatabase"):
    os.mkdir("lanedatabase")

with open("lanedatabase/lanes.json", "w") as f:
    json.dump(data, f, indent=4)

if not os.path.exists("lanedatabase/twoparts"):
    os.mkdir("lanedatabase/twoparts")

with open("lanedatabase/twoparts/axes.json", "w") as f:
    json.dump(data["axes"], f, indent=4)

with open("lanedatabase/twoparts/lanes.json", "w") as f:
    json.dump(data["R"], f, indent=4)

if not os.path.exists("lanedatabase/fullRs"):
    os.mkdir("lanedatabase/fullRs")

for Rkey, Rdata in data["R"].items():
    with open("lanedatabase/fullRs/R" + str(Rkey) + ".json", "w") as f:
        json.dump(Rdata, f, indent=4)


if not os.path.exists("lanedatabase/numbers"):
    os.mkdir("lanedatabase/numbers")

for Rkey, Rdata in data["R"].items():
    if not os.path.exists("lanedatabase/numbers/" + str(Rkey)):
        os.mkdir("lanedatabase/numbers/" + str(Rkey))

    for Nkey, Ndata in data["R"][Rkey].items():
        with open("lanedatabase/numbers/" + str(Rkey) + "/" + "L" + Nkey + ".json", "w") as f:
            json.dump(Ndata, f, indent=4)


# I am in the middle of the following simplification, now going to eat..

def simpnum(key, val):
    number = {}
    number["Ten"] = {}
    number["Ten"]["Signed"] = {}
    number["Ten"]["UnSigned"] = {}
    number["Dec"] = {}
    number["Dec"]["Signed"] = {}
    number["Dec"]["UnSigned"] = {}

    print("Value:", val)

    for Pkey, Pdata in val.items():
        number["Ten"]["Signed"][Pkey] = {}
        number["Ten"]["UnSigned"][Pkey] = {}

        print("Val: ", val)

        number["Ten"]["Signed"][Pkey]["X"] = val["Ten"]["Signed"]["X"]
        number["Ten"]["Signed"][Pkey]["Y"] = val["Ten"]["Signed"]["Y"]

        number["Ten"]["UnSigned"][Pkey]["X"] = val["Ten"]["UnSigned"]["X"]
        number["Ten"]["UnSigned"][Pkey]["Y"] = val["Ten"]["UnSigned"]["Y"]

        number["Dec"]["Signed"][Pkey] = {}
        number["Dec"]["UnSigned"][Pkey] = {}

        number["Dec"]["Signed"][Pkey]["X"] = val["Dec"]["Signed"]["X"]
        number["Dec"]["Signed"][Pkey]["Y"] = val["Dec"]["Signed"]["Y"]

        number["Dec"]["UnSigned"][Pkey]["X"] = val["Dec"]["UnSigned"]["X"]
        number["Dec"]["UnSigned"][Pkey]["Y"] = val["Dec"]["UnSigned"]["Y"]

    return key, number

if not os.path.exists("lanedatabase/simpRs/"):
    os.mkdir("lanedatabase/simpRs/")

if not os.path.exists("lanedatabase/numbers.simp/"):
    os.mkdir("lanedatabase/numbers.simp/")

if not os.path.exists("lanedatabase/numbers.simp/" + str(Rkey)):
    os.mkdir("lanedatabase/numbers.simp/" + str(Rkey))

for Rkey, Rdata in data["R"].items():
    if not os.path.exists("lanedatabase/numbers.simp/" + str(Rkey)):
        os.mkdir("lanedatabase/numbers.simp/" + str(Rkey))

    simpR = {}

    print("Ndata", Ndata)

    for Nkey, Ndata in data["R"][Rkey].items():
        print("key/data", Nkey, Ndata)

        Mdata = []
        for MKey, Mdata in Ndata.items():
            _, Mdata[MKey] = simpnum(MKey, Ndata[MKey])

        with open("lanedatabase/numbers/" + str(Rkey) + "/" + "L" + Nkey + ".json", "w") as f:
            json.dump(Ndata, f, indent=4)
        
        simpR[Nkey] = Ndata

    if not os.path.exists("lanedatabase/simpRs/" + str(Rkey)):
        os.mkdir("lanedatabase/simpRs/" + str(Rkey))

    with open("lanedatabase/simpRs/R" + str(Rkey) + ".json", "w") as f:
        json.dump(Rdata, f, indent=4)


#if not os.path.exists("lanedatabase/simpRs"):
#    os.mkdir("lanedatabase/simpRs")

#for Rkey, Rdata in data["R"].items():
#    with open("lanedatabase/fullRs/R" + str(Rkey) + ".json", "w") as f:
#        json.dump(Rdata, f, indent=4)

# Well enough, let's go on.

