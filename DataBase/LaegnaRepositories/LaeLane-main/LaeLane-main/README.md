Let me give my criticism:

- I and E boundaries should actually give square-sized images somehow, but I wanted the AI to create rather reusable code which measures the boundaries and does not expect them.

Code here is layered:
- Generator does not expect you to ever delete the generated folders as a whole; rather you could write delete scripts which delete some parts.
- TODO: right now it overwrites local README.md when you run it in VSCode menu if random folder is open in console; this is not intented and planned fix is that it will require it's own code file with signed first line to exist in folder where it's ran: it would enforce it's position right in numbers folder.
  - When this code is completely fixed, I will move it to "clean" version with manual code, which resolves any graphics generation error.
  - I looked the small and stupid boxes and thought: but this is how eyes of an AI would see this.
    - I have seen AI training images - unhumanly small, with unusably small precision, yet perfect for especially the early AI, thus they should be kind of "trivial" or "essential" to modern AI. Because AI was responsible to express those files, and reasoned itself mathematically - to fix anything actually needs a mathematical proof if you don't want to break it. So: you can ask CoPilot, and actually explain it any agenda, and in the final version every generation file is very small and the API is trivial: I did not add every fix this task needs, but this should be achieved by human-AI cooperation.
    - I want to exactly fix this automatic building not give it trivial size calculation which exists in generator.py itself and utilities.py, where numbers and waves are defined.
    - I do not even understand did it turn them upside down now, but it's it's own scientific quality sense which decides here: I cannot confirm every algorithm in it's mathematical work.
    - I really thought that it's at least *somehow* standardized, and it should be number-wise correct as much as up to us, I.E. pixel and SVG point coorinates, as well as Laegna line projection and indeed we found established standard algorithm for this kind of line drawing: my math is funnily compatible with modern engineering and use of classic and modern math, I just resolved the problems how to write them inline in different ways.

This is meant so that:
- Small-context window AI can be given examples, for example R=3 and R=4 folders deleted, and either original JSONs or CSV or SVG left for textual processor with code capability, almost trivially.
- Original Json was used to generate this, altough there are several passes of full generator contained.

Code is written so that in generative folders, where files are generated, there are also new programs to generate further layers:
- You might stop at subset of basic files more or less duplicating the original generator present in this project (written wholly by me, without internet, because A.I. did not understand me any more).
- You might generate folders and files, which have subsets: each subset selection splits the database to files, and every file has only this selection subset.
- When numbers folder is filled, there is the basic image generator.
- I probably generate more simple numbers and images in folders which are marked "simplified", because I have to simplify the task now, for example manual code should generate basic image metadata - implies that size, projection, and various rules are needed for each R, to reason how AI needs to position the graph.
- If I match PNG and SVG pixel-by-pixel, and keep simplest forms, image would be reversed easily: in way that image counts downwards-bigger, but the number dimension is upwards-bigger. There are design questions and CoPilot has solved them all: I can only confirm that numbers in SVG files, reading it and asking every question from CoPilot does it really represent this number, I can agree it's somehow mathematically correct.

Simplification would basically mean:
- Right now like two frequencies are *added*, which forms projection to lower dimensional scale which distorts it.
- What is *actual*, both dimensions need to be simplified to half-dimension presicion, and the result added so we take the *average* of the function and model it in strict two-dimensional world.

# LaeLane

Lane: linear, calculable, mathematically simple index of higher realms, such as two-frequency bands of linear and exponential function.
- Single binary opposition is shown here: lin=>exp. Log=>exp or any other differential<->exponential order (measured in "octaves" in Laegna language) just repeat this relation, and Laegna base logic is for trivial oppositions brought into continuums by math.

Line: the projected output.
- As Lane is to simplify and linearize a Line, it cannot exist without. Line exists in linear, single band, where operations are not guaranteed to be linearly safe even if they exist.

- [CanvasMode](CanvasMode): here, Lane database is given in long form, many files and space usage, but AI and robots as well as humans should be able to utilize this. It can verify results multiple times.

- [LaegnaLane](LaegnaLane): here, learn about Lanes.
  - [LaegnaLane/SrcAIPnP](LaegnaLane/SrcAIPnP) - Sheep Counter database, connectible with Lane database based on Laegna number and R index as id.
 
- [LaneDatums](LaneDatums): full implementation of Lane database, but minimally with less output formats, and maximally in sense then this format has to contain it all.
  - Files and results might be simpler to analyze, reuse, or develop to different directions from CanvasMode.
