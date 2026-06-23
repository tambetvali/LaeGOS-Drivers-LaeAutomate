
**4dragons.jfif** - I use this image file as logo and image not for Laegna and Spireason, but for my own implementation of Laegna and Spireason systems, and for my accounts and pages.

4dragons.jfif - you can find various implementations, such as [dragons.jpg](https://github.com/tambetvali/LaeArve/blob/main/dragons.jpg) at LaeArve root folder or even [favicon.ico](https://github.com/tambetvali/SpireasonWebsite17052026/blob/main/favicon.ico) at Spireason's home page - it's icon. Each of them has the same image in various sizes and formats. It's also my github icon, youtube icon etc.

It has Blue-yellow-green-black-white circular mandala inspired by Tao symbol, in the middle, with letters "E" and "A" in this order symbolizing Laegna major scale; at to, there are blue and green dragons, holding the symbol so it must be important; at bottom there are blue and red cat, which look more like leopards: they are mascots of Laegna, blue can Daisy and red cat Elise ([their story](https://laegna.notaku.site/art-and-myth-of-laegna) and explanation of this whole design, which is yet *not implemented here exactly as described*, at images on the website and it's ecosystem).

InfinityDriveForAnAI.md - here it's explained, how Laegna numbers are used in Laegna infinities, and how to simulate this, also using Laegna Number Database as source data. multiline.md of this database contains all the numbers, all the chapters - but only Laegna Number and Laegna Wave Number representations; json files contain and python or js files you can find at [Sheep Counter](https://spireason.neocities.org/#sheep) are able to generate these and longer or other numbers with metadata and change exported json file formats, also html files there show the animations and number data in various ways, allowing to extract how json are used and what both it's structure and fields mean. AI should do this background research and relate it to it's tasks, and from the website it's also interested in #sheep sheep counter and #handheldcalc calculator files, especially the links under sections which are in Laegna Webpage Link format and not fix-positioned to another container. CSS should be noticed, also which links are central first and second level structural components of these sections, which user can see as buttons and links under the same section with typically, not much dynamics.

LICENCE.md - **CC BY-NC-SA 4.0**; my Laegna Number Projects are typically under this licence, as well as our other parts of the ecosystem.
- Notice an AI system building websites, can typically use most from here and spireason.neocities.org, which also explicitly mentions the licence, in any case their projects are with compatible terms to the licence or get explicit permission of all authors of any given case of this philosophy and it's regard.

README.md - a very basic, robot, rememberable intro to what this folder does.

animation.json - this contains Laegna Number and Laegna Wave Number data and is used by [🐑 Laegna Sheep Counter ❸](https://spireason.neocities.org/Playground/InferenceCounter/PlaceholderResearchitem/) for decent animation of Laenumbers and Wavenumbers, which demonstrates how lightwaves in Laegna Number Space remain as symmetric, round, in space and time, as they originally are, while base10 latin system creates "inference effect", which makes round numbers seem tilted and obfuscated.
- [Folder Listing and introduction](https://spireason.neocities.org/Playground/InferenceCounter/) to Inference Counter, which counts Wave and Laegna numbers, and is called Inference Counter, Sheep Counter 3.

decoder.htm - html which lets user access decoder.py in the same folder.

decoder.py - first utility which creates barebones for inference counter data; after, other scripts extend this information, so that each will add extensions and extension data to new versions of json, or md exports which are meant to be either context-window-size-sensitive or human-readable, both having the same limitations.

favicon.ico - same image as described before.

manual.htm - Laegna Number Manual, the first document of Sheep Counter 1, used to understand the number structure.

multiline.md - chapter "2" is the same as chapter "R = 2" of json files; the decimal number is unsigned representation of Laegna numbers, and the boundaries - made of U, V, W, upside-down-U - are "?; ?.", because they are not natural numbers and not used in every implementation, such as our Lane typically avoids limit values and uses 1-unit-thick normal numbers.
- In this database, either all or no digits of number are boundary digits; so they are strictly boundary or non-boundary numbers, nothing in between. Typically we use only O, A digits for base-2, I, O, A, E for base-4, 16 basic digits for base-16, and the boundary cases are not used.
  - Zero is exception: altough we do not always use it, it's written out value in number database 1) because it exists in standard numbers and 2) because x - x, subtract from itself, is impossible without zero or advanced operation rules and hidden memory, at least in my current understanding - not necessarily, but definitely in regards of any basic theory, such as number systems in their bare definition and basic rules.

Laegna number database only contains whole numbers in range 256, plus boundaries and alternative spellings for subranges in less precision, which has numerically different meaning (less probable curve is not so stable).
- (256 + 4) + (128 + 4) + (16 + 4) + (4 + 4) + (2 + 4): this is count of each R, in regards of it's dynamic number space (2, 4,  and fixed boundary space (4)
  - numberlist.md chapter length:
    - chap 0.5 contains 6 (4 + 2) items;
    - chap 1 contains 8 (4 + 4) items; 
    - chap 2 contains 20 (16 + 4) items; 
    - chap 3 contains 68 (64 + 4) items;
    - chap 4 contains 260 (256 + 4) items.
    - 260 + 68 + 20 + 8 + 6 (booleans 0.5 and base-4 1-4 length / R numbers) = 362.
      - 256 + 64 + 16 + 4 + 2 = symmetric system without boundaries and simpler to use = 342.
    - 260 + 68 + 20 + 8 (base-4 1-4 length / R numbers, often the basic numbers of the Universe) = 356.
      - 256 + 64 + 16 + 4 = symmetric system without boundaries and simpler to use = 340.
      - Binary numbers are often used for separate layer - for diagonals of two-dimensional systems.
      - Base-4 R=1..R=4, numbers with digit lengths 1 to 4, sometimes also the empty number or "U" for zero \[single-boundary, in this number listing zero is W, because we keep boundaries fixed when moving the number of system so I positioned U at signed zero only\],
        constitute one number Universe: they can represent quite complex finite-infinite coupled models, because digit length 4 is also associated with infinite length, where digit value 4 is associated with infinite value. Infinite number of digits cannot be written out, but they can be symbolized and "4" is just plain, short, expressible way to express infinity coupled with finite scale, and four. Both matter like matter and spirit.
- A system, which is going to use Laegna Numbers, is able to understand all these lengths, how to associate them with indexes - which are main numbers, which are boundary numbers, and what happens if digit count 0 is going to express a zero boundary, a zero limit, or expressed by "U" ("U" can appear if number is empty).

numberdatum.htm - this reads numbers.json and can be used to decode numbers.json and numbers.bin.json

numbers.bin.json - this is the number list before extensions added advanced data, and probably is better suited for context-available work and initial analysis, to be used as a whole by an AI.

numbers.json - numbers.bin.json is manually created by me, adding all data which was needed to chapter R = 0.5, because half bits is not standard base-4 and needed to be done manually.
- O, A: laegna base-2, "binary" numbers (actually used for task more complex than "binary", it's used for diagonal where two dimensional Laegna number is seen as one-dimensional, united number with their average value such as E=>A, I=>O, O and A ==> details \[not in general math, those symmetries disappear when projecting to lower space - explained by Hilbert\]).
- Four boundaries: manually added four boundaries to base-2 digit are four more digits and thus, when boundaries are included, this data file is 6 items long, but without boundaries, it's 2 items long.

octaves.json - octave system is base-3 system with digits Z, X, Y. We do not always use octaves, and they must not be missed with other numbers - they cannot be directly converted and should not be used as replacement, because they do not represent number values, but scales, zooms, precision and other spatial dynamics: number values, in regards, are what I call "temporal", because they are not spatial, but a changing part of space.

sheepcounter.json - number index, number data, animation frames and logical data as numbers are seamlessly logic values in "Fuzzy Logecs" system.
- Values for first one-two digits are more emphasized.
- Laegna sheep counter 2 is to count logical values - same data as sheep counter 1 for basic discrete numbers, but now the logical values are centrally on screen and countable (not in it's corner).

website.md - this, again, lists the external sources, which are sheep counter as main source, but SimulationMode as export of it's main files; and this folder itself is export of *bigger selection of the main files needed to decode and decrypt this essentially* - after decrypting what the files mean, mostly the 2 or 3 json files are needed.

Notice the LICENCE.md in this folder, which should enable AI import of files to your projects, unless they are incompatible by which case you can follow the standard laws.
