# Lane Counter

***Laegna Lane Counter*** will count Laegna Lanes, ordinary lines in Laegna space vs. their Natural projections, Lines in Latin Euclidean space.

It's kind of "Sheep Counter 5", because we are specifically interested in ordinary Lanes in range R = {0.5, 1, 2, 3, 4} - same R values (digit lengths) are used in each sheep counter. Second, and moreover: it's meant to count only discrete, ordered Lanes in simplest signed and unsigned spaces. This means I had to work to create one normalized and computable model, which will be used in base calculations and modulations - especially in computational or discrete counting spaces, but their growth is kind of trivial, in sense that for example division by infinity would turn discrete points to continuous infinitesimals - so zeros that almost an abstract concept, but as a class construction and physical attitude, it's real enough.

Counter is programmed in Python, and it's expected that Sheep Counters (SCs) contain all the countable numbers between R = 0.5 (binary 1 digit) and R = 1 to 4 (lae-4 1 up to 4 discretely counted digits). Binary 1 digit will be converted to R = 1 through applying it on both channels and thus, the diagonal.

I am not interested in boundary values, so best way to associate them with Laegna numbers database is to count n ^ 2 digits of binary data, and add padding if odd digit number is given, could simplify it: numbers beyond that behave like irrationals and I'm not interested in them in ordinary counting, no way. I would lose all developments.

To not waste your time, is python files: the output should be implied into sheepcounter's json files, and boundary values are equal to actual boundaries, where middle curved zero is not counted but implied by the surrounding space, being an accelerated dot of it's left and right digits, so that digits won't lose their symmetries and space. In ordinary math, although, this might seem too complex - numbers become rather abstract points, which is mathematically consistent.

The chosen system does not express too much what it expects *metaphysically*, although it aligns somehow into each metaphysical conceptional unit space.

Files follow, and their output is given by default along, as it's only a few numbers as a number database add-on, and I think I can write extensions to both number databases, either into their initial code or as add-on of this code, and I think rather the separate code file given here can be converted to initial syntax to be enabled or disabled right when database is created: I leave boundaries inside here, thus each item also gets it's pair of unique id's and I append them to both json files here, where final output folder contains two json files with additional number data to be used in advanced generations. I might choose several alternative types to represent it, and allow enabling and disabling internal functions for generating various files. I copy some code from small number database extensions, and mention this.

***utilities.py*** - generates Laegna Lane Point Database.

***generator.py*** - formats to json and writes the database into a file.

***lanes.json*** - all the lanes.

# lanes.json, specifically

This file is not optimized Laegna Lane Database, but single file containing all the items. As I see what is needed, I also add some specific, condensed and optimized versions, but this current version is simply *easiest to read*.

## Axes, the first dict of this json file

UnSignedTen - contains unsigned laegna lane point data, the linear (id) *imag* representation
SignedTen - contains signed laegna lane point data, the linear (id) *imag* representation
UnSignedDec - contains unsigned laegna latin line point data, natural non-linear, *real* representation
SignedDec - contains signed laegna latin line point data, natural non-linear, *real* representation

Each of them contains laegna numeric values of R and T:
R, length of each piece, is also *the number of X axe point in exponentially growing axe structure.
T, content of each, shows that the lane or line would pass this point as it's point number R, if the point identifier matches the exact digits *until then* - so for number IOAE, it would pass through points with Y values of I, IO, IOA, IOAE in order, corresponding to some exponent at X.

## Numbers, the second dict

Numbers are calculated on Axes data, and contain:

Chapter R: numbers are divided into chapters R.

Number R index: R is indexed to elements by their numbers.

Below this is the point number, then:
- Ten
  - UnSigned: matches point from SignedTen
  - Signed: matches point from SignedTen
- Dec
  - UnSigned: matches point from SignedDec
  - Signed: matches point from SignedDec

Each of these 4 branches have the following elements inside:

- SrcAxeY: such as "Axes.SignedDec["1"]" - which axe is used, as string pointer to axes.
- SrcY: such as "Axes.SignedDec["1"]["I"]" - exact point data in axes database.
- X: such as 2
  - This is calculated X at this point, the *center of it's unit*
- Y: such as 1
  - This is calculated Y at this point, the *center of it's unit*

Center of unit: in square field, each point with it's X and Y means coordinate exactly in the center of square with these coordinates.

Notice that pointing each element to axes database, altough raising contextual memory, creates an AI more context about connections and associations, which are directly visible and learnable.

# Extending lanes

For "Lae" lanes, they are linear:
- The given identificator square contains qualitative number data.
- It can be extended up and down as fractal.

Example:

O A - points 0 and 1

OO OA AO AA - extended to two grids. Notice that current OO = ex O, current AA = ex a, which means both are bounded.


For "Dec" lanes - this is not really decimal, but Laegna system which carries natural data similarly to decimal numbers - mainly, does not linearize exponents because if we only linearize them, we do not get actual answers:
- Here, fractals need to be build on first bits of digits (exponent) and second bits (linear) independently, then the same algorithm used as now (higher and lower frequency need to be mapped separately to holograms, because both are *internally linear*; result, indeed, might lead also to optimized math which does this somehow on both simultaneously, but this hardly works as definition, so we build the primitive one).