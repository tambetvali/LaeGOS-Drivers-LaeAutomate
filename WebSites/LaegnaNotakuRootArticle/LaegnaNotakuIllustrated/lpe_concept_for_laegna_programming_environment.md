# LPE: Concept for Laegna Programming Environment

This is the number generator code: this version only generates sensible Laegna numbers, but it does not know neither operations nor the decimal representations - it’s rather a very simple structure for definition of basic Laegna numbers in some of the simplest format (my current task is to generate more numbers, but based on this one, you should be able to do):

```python
import math
import numpy as np
import mpmath as mp

base16 = ["GFEH", "CBAD", "QPOR", "KIJL"]

class Digit:
    def __init__(self, fmt):
        self.fmt = fmt
        self.x = np.random.randint(0, fmt.f)
        self.y = np.random.randint(0, fmt.f)
        if np.random.randint(1, fmt.f * 4) == 1:
            self.ux = np.random.randint(0, 2) == 1
            self.uy = np.random.randint(0, 2) == 1
        else:
            self.ux = 0
            self.uy = 0

    def __str__(self):
        # Base 2
        if self.fmt.l:
            if self.ux and self.uy: return "Ü"
            if self.ux: return "U"
            if self.uy: return "Ẅ"
        if not self.fmt.l:
            if self.ux and self.uy: return "?"
            if self.ux: return "0"
            if self.uy: return "9"
        if self.fmt.f == 2 and (self.fmt.w):
            if self.fmt.l:
                if self.x == 1: l = "A"
                if self.x == 0: l = "O"
                if self.fmt.d == True:
                    if self.y == 1: l += "A"
                    if self.y == 0: l += "O"
                return l
            if not self.fmt.l:
                if self.x == 1: l = "2"
                if self.x == 0: l = "1"
                if self.fmt.d == True:
                    if self.y == 1: l += "4"
                    if self.y == 0: l += "3"
                return l
        if self.fmt.f == 2:
            if self.fmt.l:
                if self.x == 1 and self.y == 1: return "T"
                if self.x == 0 and self.y == 1: return "S"
                if self.x == 1 and self.y == 0: return "N"
                if self.x == 0 and self.y == 0: return "M"
            if not self.fmt.l:
                if self.x == 1 and self.y == 1: return "4"
                if self.x == 0 and self.y == 1: return "3"
                if self.x == 1 and self.y == 0: return "2"
                if self.x == 0 and self.y == 0: return "1"
        if self.fmt.f == 4 and (self.fmt.w == False or self.fmt.w):
            if self.fmt.l:
                if self.x == 3: l = "E"
                if self.x == 2: l = "A"
                if self.x == 1: l = "O"
                if self.x == 0: l = "I"
                if self.fmt.d == 2:
                    if self.y == 3: l += "R"
                    if self.y == 2: l += "O"
                    if self.y == 1: l += "P"
                    if self.y == 0: l += "Q"
                return l
            if not self.fmt.l:
                if self.x == 3: l = "4"
                if self.x == 2: l = "3"
                if self.x == 1: l = "2"
                if self.x == 0: l = "1"
                if self.fmt.d == 2:
                    if self.y == 3: l += "8"
                    if self.y == 2: l += "7"
                    if self.y == 1: l += "6"
                    if self.y == 0: l += "5"
                return l
        if self.fmt.f == 4 and self.fmt.d == True:
            return base16[self.x][self.y]

        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Digital:
    def __init__(self):
        self.setf(np.random.randint(1, 3) * 2)
        self.setd(np.random.randint(1, 3))
        self.setl(np.random.randint(1, 3) == 1)
        self.setw(np.random.randint(1, 3) == 1)
        self.generate()

    # Set the frequency; for example 2 is base-2, 4 is base-4
    def setf(self, f):
        print("f: ", f)
        self.f = f
    
    # Set the dimension; 1=real and 2=complex number
    def setd(self, d):
        print("d: ", d)
        self.d = d
    
    # Switch between Laegna and Decimal representation; True if Laegna
    def setl(self, l):
        print("l: ", l)
        self.l = l
    
    # True if digit is RT double-character, false otherwise
    def setw(self, w):
        print("w: ", w)
        self.w = w

    def __str__(self):
        ex = ""
        for n in self.number:
            ex += str(n)
        return ex

    # Randomly generate a number
    def generate(self):
        length = np.random.randint(1, 101)
        self.number = []
        for a in range(0, length):
            self.number.append(Digit(self))


num = Digital()
print(str(num))
```



Laegna Numbers

Examplified Manual

Denary

Signed

• O: -1; up; limit to -1 or -Zero

• U: 0; middle (inwards); limit to 0 or Zero!

- A: 1; down; limit to 1 or +Zero
Unsigned

• U: 0; middle (inwards); limit to 0 or Zero!

- O: 1; down; limit to 1 or Zero
• A: 2; up; limit to 2 or 2 Infinitesimals

Tenary

V: Upside down U

Unsigned

• I: -2; down; limit to -2 or -Exzero

• O: -1; up; limit to -1 or -Zero

• U: 0; middle (inwards); limit to 0 or Zero!

- A: 1; down; limit to 1 or +Zero
• E: 2; up; limit to 2 or +Exzero

• V: 2 · -2; outwards; limit to between 2 and -2 in Order; or Exzero!

Signed

• U: 0 · 5; inwards / upwards; limit to between -2 and 2 in Order; or Izzero!

- I: 1; up; limit to -1 or -Zero
• O: 2; down; limit to 1 or Zero

• A: 3; up; limit to 2 or 2 Infinitesimals

• E: 4; up; limit to -1 or -Zero

• V: 5 · 0; outwards / downwards; limit to between 2 and -2 in Order; or Exzero!

Decimal Signed

• 9A: Velocity=-V (imaginary receiver)• 1: Velocity=I

• 2: Velocity=O

• 0A: Velocity=U

• 3: Velocity=A

• 4: Velocity=E

• 5: Acceleration=I

• 6: Acceleration=O

• 0B: Acceleration=U

• 7: Acceleration=A

• 8: Acceleration=E

• 9B: Acceleration=V

Decimal Unsigned

• 0: Jump to 9 (Velocity=0); Value=Velocity

• 1: Velocity=1; Value=Velocity

• 2: Velocity=2; Value=Velocity

• 3: Velocity=3; Value=Velocity

• 4: Velocity=4; Value=Velocity

• 5: Acceleration=5; Value=Acceleration

• 6: Acceleration=6; Value=Acceleration

• 7: Acceleration=7; Value=Acceleration

• 8: Acceleration=8; Value=Acceleration

• 9: Jump to 0 (Acceleration=9); Value=Acceleration

Decet

X=X

• 1: Y=X; exZ=exZ

• 2: Y=Y

• 3: Y=Z

X=Y

• 4: Y=X

• 5: Y=Y; exY=exY

• 6: Y=Z

X=Z

• 7: Y=X

• 8: Y=Y

• 9: Y=Z

X=exX

• 0: exX=exX

Coordinate Systems

Unsigned Coordinate System

X=1

Y=2

Z=0

Signed Coordinate System

X=0

Y=1

Z=-1

Z can be seen as 2 (infinity crossover with E) in Signed

Coordinate System; how could it be 3 in Unsigned System if 3 is not specifically an infinity around here, unless it’s Decimal

Coordinate System, which is particularly not Laegna Number System! Z can be Y square very well, such as a value symmetric to YY or Y^Y, which as you see have the same number notation YY with symmetric digitalization, because position of Y in Y^Y is definitely before position of Y in it, respectively pointing to 2 Y’s.

Logex Ten

Logex is a Logic Machine and for it is Ten and Tensor given here:

Logex Tensor:

In brackets of Names: optional letters (implement full syntax of alternatives, such as “/”).

Multiword names are allowed, which is IDE linguistic modification and AI meaningful analysis to

proceed with that, foresee that and junk-analyze, clean and stylify the results, optionally or

potentially by user confirmation, fix them.

Interface Tensor for Tensor(s):

- Input Portal: Map of Combinators (iterate combinations)
◦Callback: automatic gradient backpropagation

- Receiver Map:
◦Input: from Input Portal

◦Custom: Integrator receiving Combinators

▪Integrator: receiving Combinators; executing Tensor

Database

Logex Combinator:

Interface Combinator for Combinator(s):

• Integrate list of all combinations given, which yield some results

◦Aggregator: Give if the result thus combinator, in same but componentizable into two dimensions: the result is what is the logecs ponegate value of this combination, whether it’s I, O, A or E, where zero (U or reverse-U) means it is not given in the list, or given in U-extended listing defined by user as Combinator table header and content item, where content is class and item is it’s class listing.

◦Processors: Which classes are working to process this item, classes in instances in particular, but which can be seen in class item listing. Even if written in file, processors must remain as APIs containing enough code for files.

Logex Memory and Files

Links are either Memory or File Blocks or shared Internet items, including intranet and “local” community as chosen by AI from internet and local network; each File or Folder item is made of Blocks, which can be either files or folders, visible subitems to exter (outwards) files and folders.

File API or it’s driver or mother program can provide visible (given the file is open or loaded as module or executed as

Notice: all these numbers are practical pieces to integrate infinities, normal numbers and zeroes into continuous number spaces, and not to compress your numbers with maximum tightness - Laegna can help here as well, but it’s not my current primary intent (well simply take all possible dimensions, map them to only one dimension and do not use frequential system but fractal system, where A and AA are not same but it’s growing).



Octave numbers:



For example, if you want to number octaves (where the better idea is to zoom into U and V with them, they can be attributed some numbers):

```markdown
  ZZ = -4
  ZX = -3
  ZY = -2
(X)Z = -1
(X)X = 0
(X)Y = 1
  YX = 2
  YY = 3
  YZ = 4
```

In the actuality, they form rather a fractal than number systems! In all cases, you can continue this one infinitely. This is: because they are rather for other purpose, it’s hard to write them as numbers - in most simple case you can use each Z or Y for one zoom operation into your number system or out from it, and most typically you use 1-digit number; you are free to specify your specific zoom operations to use it for your comfort.



Base-1:

```markdown
A = 1
AA = 2
AAA = 3
…
```



Base-2 (notice carefully that this is not binary system - A, AA and AAA are powers of two, not 10, 100 and 1000; this is to support frequential system of Laegna; any I or E digits will be moved, virtually, to previous digit and added there, this can be a chain effect):

```markdown
OOO - 1
OOA - 2
OAO - 3
OAA - 4
AOO - 5
AOA - 6
AAO - 7
AAA - 8
```



The base 2:

- Unsigned form is rather one big knot, where OOO and AAA are -1 and 1, but the rest of the numbers is some complex magic of Laegna, which is introduced in the programming book, but I have to take time for this - why you need base 2 at all.
- If, for 3-digit numbers, you divide them by 4 and subtract 1, you get the smooth version of signed numbers, which is not producing such knots ..unless you look carefully haha :P


The base 4:

Signed:

```markdown
EEEE = 16
EEEA = 15
EEAE = 14
EEAA = 13
EAEE = 12
EAEA = 11
EAAE = 10
EAAA = 9
AEEE = 8
AEEA = 7
AEAE = 6
AEAA = 5
AAEE = 4
AAEA = 3
AAAE = 2
AAAA = 1
OOOO = -1
OOOI = -2
OOIO = -3
OOII = -4
OIOO = -5
OIOI = -6
OIIO = -7
OIII = -8
IOOO = -9
IOOI = -10
IOIO = -11
IOII = -12
IIOO = -13
IIOI = -14
IIIO = -15
IIII = -16
```

Unsigned:

```markdown
II = 1
IO = 2
IA = 3
IE = 4
OI = 5
OO = 6
OA = 7
OE = 8
AI = 9
AO = 10
AA = 11
AE = 12
EI = 13
EO = 14
EA = 15
EE = 16
```



Digit representation of base 4:

```markdown
E = AA
A = AO
O = OA
I = OO
```



Digit representation of base 8:

```markdown
Unsigned 9: from top, back to bottom (circle forward)
* Unsigned 9 can also mean the whole 48 (5 to 8) group of numbers
* such as center or random number of them.

Acceleration:
8 = EAA; acceleration = E
7 = EAO; acceleration = A
Neutral acceleration (signed 0)
* It's either any of numbers in this group, or normally 7 or 6.
6 = EOA; acceleration = O
5 = EOO; acceleration = I
Outer acceleration (signed 9)
* Normally 8 or 5.

Velocity:
4 = IAA; velocity = E
3 = IAO; velocity = A
Neutral velocity (signed 0)
* Any member, or normally 3 or 2.
2 = IOA; velocity = O
1 = IOO; velocity = I
Outer velocity (signed 9)
* Normally 4 or 1.

Unsigned 0: from bottom, back to top (circle backwards)
* Unsigned 0 can also mean the whole 14 (1 to 4) group of numbers
* such as center or random number of them.
```



Complex number (where it’s defined by OPQR axe, which is mentioned in case of configuration):

```markdown
O: T=A; R=I
P: T=O; R=O
Q: T=I; R=A
R: T=E; R=E
```

Complex number shape:

- When it’s outwards, inwards, upwards, downwards positioned from other digits:
- It’s always inversed.
- The number order fits the criteria of inversing and reversing - result is the number with same shape.


Den

```markdown
O: -1
A: 1
```



Den (R, T)

```markdown
R = O => R = -1
R = A => R = 1
T = O => T = -1
T = A => T = 1
```



Ponegative numbers

```markdown
Polar ponegative, might be associated with polar numbers:
I Negotion; Dens: OO
O Negation; Dens: OA
A Position; Dens: AO
E Posetion; Dens: AA
- Polar: it creates a number circle, and on the poles there is ice!

Linear ponegative, might be associated with linear numbers:
I Negotion; Dens: OO
O Posetion; Dens: OA
A Negation; Dens: AO
E Position; Dens: AA
- Linear: it grows in the same direction indefinitely, so it rather looks a little
like binary.

Notice that if both numbers have the same primary Dens at same number position,
they are not at the same ponegative position.

In complex numbers, typically, ponegation is made with the same real numbers, not the
same complex value. This is at least how I do it, because why to invert at all if I
then would start to reduce this operation with other calibrations :)
```



Even-odd complex numbers:

```markdown
Even-odd complex numbers are made of RT pairs, either separated by space, color or
number position (herein):

Decimal system: two decimal digits for each, between 1 and 8 (18)
Decimal system: two decimal digits for each, between 14 48 - first digit between
  1 and 4, second between 5 and 8; 48 might be in real or complex order.
Dens and base 2: two digits for each; Den usually knows R and T very precisely.
Reals: two digits of IE can be used for each group, projected to real and imaginary
  axe, but the second group is not inversed in any way.
Complexes: one digit of IE followed by one digit of OR in each group.

Example complex numbers:
47584393 - long decimal complex, with 18 on both positions
63817352 - short decimal complex, with 14 and 48 on separate positions
AEEAOIAE - real complex
OARAQIPO - imag/real complex
```



Complex matrix numbers:

```markdown
These digits are two-dimensional at base 4 (* 4) - base OIRE:
EFGH
ABCD
OPQR
IJKL

These digits are two-dimensional at base 2 (* 2), and rather bigger than last group:
ST
MN

These digits are two-dimensional at base 3 * 3 - base ZY^2:
123
456
789 - move this group up, and the last column to beginning, for signed number.

Additionally, U and V for Laegna complex and 0 and 9 for Latin complex:
* Are used to access the ZY coordinate systems; numeric value is given in odd systems,
but notice it does not change the order much and enters into one of two possible
positions typically; if you program it later you might be better off.
```



U and V, 0 and 9:

```markdown
Initially, define them as taking the averages:
- For signed number, U is in the middle and V is in the end, where U connects inwards
  and V connects outwards.
- For unsigned numbers, U is in the beginning and V is in the end, where U connects
  circle / wheel backwards, V connects it frontwards, effectively turning it to a wheel,
  either moving in Z circles (evolution, logic sometimes appears), standing in X (ration,
  logic rather is constantly there), accelerating in Y (logic of X looks like
  evolutionary phase when zooming to Y).
  
At each position of U or V, you create a random selection, where you don't know which:
- To create a zero-based number, take an average of those randomizations to cancel the
  random factor, this equals to taking zeroes one octave down but you still have the
  randoms.
- Use space or another character to denote if each number is random.

U and V for complex numbers:
- Both axes are random at that position, for example U might be any number in the
  interior of both dimensions, where V can be the exterior.
  
For example, given NMST is two-dimensional base-2 matrix, for base 2 U exist, but not V;
given this matrix: U simply means random number chosen from any of the four.
If you write complexes with 2 digits or U's with more digits, you can be more specific
and separate the axes.
```



