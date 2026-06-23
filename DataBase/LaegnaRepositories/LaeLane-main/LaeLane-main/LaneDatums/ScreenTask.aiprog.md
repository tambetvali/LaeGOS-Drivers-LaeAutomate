[Calculator](https://spireason.neocities.org/#handheldcal) selection at Laegna Home Page now has [Prototype Calculator](https://tn99tkkgqg.youware.app/) available straight off, so this should provide an initial experience of Laegna Numbers. Purpose of this is to understand, how laegna number systems directly and trivially map one another - this is kind of parallel thinking and makes it usable to switch dimensionality, reducing or specifying it.

--------------------

This was also not initially done by copilot - I need to program the basic logic of keyboard myself. Now I vaguely have idea of things I need to code myself to keep the quality up.

--------------------

Use spireason.neocities.org as we create a widget to be positioned at https://spireason.neocities.org/#handheldcal, initially, so that everybody can copy the code.

It is thin by height, but 100% in width:
- It contains small screen, which can initially have 4 characters, but grows in length up to 16.
- It has different background colors for each letter, so use fixed-width Laegna (orange, schoolbook style but now more like piece of technology) calculator-style font and repeat background colors for letternum % 4 groups in this order as pattern, each color 1-letter-wide exactly: yellow, red, green, blue; added letters: again yellow, green.. indefinitely (or up to maximum 16).

It has two lines, screens and buttons:
- Each screen can contain up to 16 digits, but backfront digit is not restricted in length, but free-form string of letters O and A. It can be empty.
- Under each screen, there is separate keyboard.
- Next to each screen, there is a button to make it empty - a little symbol for Clear, where normal calculator text like "C" is too abstract.

First screen shows the underlying data structure directly:
- O
- A

Under each O on screen, the screen fits also a little black circle; under A there is white circle. In case it's same-colored to letter's background color, it melts to it and this is important.

Second screen has:
- I: for "OO"
- O: for "OA"
- A: for "AO"
- E: for "AA"

So if you enter more than 8 letters here, base-2 (first) screen becomes red and from 8, it does not accept it's input and all buttons appear grayed-out; if you delete one digit on base-2 screen, it deletes everything after it's own 15th digit so it's last digit is available: on base-4 screen, if one digit is deleted at base-2 and 15 left, there are 7 base-4 digits and one base-2 digit in small-caps version of it's letter (at 16 of total digits, even such digits appear out-of-space, and there should be little space after screen for single "..." letter of utf-8 - no graphics should be used - which is gray if there are no more digits, but black - in case of white background both - in case there are digits beyond the screen).

Last screen is base-16 and thus, 4-digit binary groups are used respectively, as in normal conversion base2 <-> base16 known in computers as direct map, so it is direct map in my system:
- K, J, I, L: this group, if first two digits of group are OO.
- Q, P, O, R: this group, if first two digits of group are OA.
- C, B, A, D: this group, if first two digits of group are AO.
- G, F, E, H: this group, if first two digits of group are AA.

Show matrix: count from 1 to 4, I to E, from down to up as in math not programming order of Y, and from inside group, from 1 to 4, in normal order, like X, which grows in writing direction.

This screen, if it has 16 letters:
- Second, base-4 screen would show first 8 letters only, as it's 16 letters, with column first and row second IOAE conversion.

Bullets must appear below IOAE:
- I: Yellow
- O: Red
- A: Green
- E: Blue

Two bullets below hex:
- IOAE bullet of it's first two bits, a first base-4 letter conversion
- IOAE bullet of color of it's second two bits, the second base-4 letter conversion

This is reliable and robust, and there is one way to understand it.

Under each screen:
- Under first screen, two buttons to enter O and A digits, and <== with proper utf-8 letter to show backspace of little, nice-symbolic calculator rather than real factory product, in Laegna orange symbolic schoolbook style (spireason.neocities.org - learn how we designed Laegna, me and the AI).
- Under second screen, four buttons: I, O, A, E, and <==.
- Under third screen, four buttons appear: G, B, O, L and <==; this is kind of "title row" of working buttons - diagonal is important understanding of diagonal systems. Diagonal of second screen is I, E, by the way. When four buttons are hovered, they extend downwards: keeping the four at the top, but now making them slightly more bold without affecting their size

On any screen, the delete letters key simply deletes corresponding number of bits - if there are yielding binary repr. bits in small-caps, the remaining view would still have same number of yielding bits as it does not target coherence on screen but is easy, robust button - base-2 button deletes 1 OA bit from original string, base-4 button deletes 2 OA bits and for 3-digit number, 1-digit number remains so it's still 1 binary repr. bit, finally base-16 button deletes always 4 digits, and if 4 from 7 is deleted 3 is left - not 4, as if "cut to last round number".

No keyboard can enter more than it's screen allows, so for extensibility we do not limit string length, but indeed user can use third keyboard to enter 16 letter string in it's own terms, which is then 16*4 = 64 OA bits, but so the string is limited to 64. If now, one last digit is cut from base-2 screen, it's own last digit is cut and all what follows simply forgot from beginning of it's operation - string, before removing it's last letter, is already cut to max 16 digits on same screen, which means 16, 32, or 64 underlying digits in it's "permanent" (locally, for non-stateful machine, the "storage" format and singleton, permanent through it's operation on different screens and keyboards). spireason.neocities.org/#sheep - sheep calculator has json files with exact meanings to Laegna number systems, it's base-2, base-4 and base-16 encoding, and the counter 1 with it's json files already represents this. Base-2 has one tiny handmade json: you can use all this to simplify your understanding when coding.

When trying to add to screen which is already full, either screen is not cut first to 16 - or otherwise, if it cannot add (true if full), it would use 16-digit limited string of it's own base (2, 4 or 16), but it would not replace the screen value if it yields error: not add.

Flat, schoolbook buttons, each letter has filled circle little, but not too little - easily visible - bullet below it, at same color as bullets below characters on screen.
