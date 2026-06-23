This was the task for json file generator, with pngs and svgs tasks already contextually known:

Can you now write a last driver, also mocking it's more or less the same by external interface:

It creates the same interface, but now the extension is "json", so it's "laejson.py"

It contains the SVG code, including both line connected by points, and hooking into laesvg.png to do this - second, it will contain CSV table. It has all 5 graphical versions as json string svgs, and one multiline string for csv which has headers "X, Y" and then points such as "0, 0", "128, -74" etc.

So the json file name and folder are given, then the points added, and while CSV has one variant without background or color specified, SVGs have 5 variants.

Additionally, based on ".json"-removal which is case-insensitive, all 5 complementary "png" and "svg" filenames are generated and supposed to be in the same folder, as well as one csv filename.

All the filenames are included, with format prefixes "I", "O", "A", "E", "U" always used as dictionary keys of these formats, but not excluded from the internal id where they repeat, so that space for each format exists; SVG is given "U", "unspecified" to another degree, as it's standard and single format key which exists as unique key altough it's the only format of this format.
