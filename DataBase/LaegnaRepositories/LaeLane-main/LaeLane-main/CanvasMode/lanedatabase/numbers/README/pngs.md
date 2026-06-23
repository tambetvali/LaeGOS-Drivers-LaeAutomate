This was the task for CoPilot to assist in png file creation:

Now, for LaeLane:

How to create image of size x * y, for PNG format, and draw lines between points in such way that no antialiasing is done, and shortest-nearest-neightbourhood, Laegna pattern is used to connect the dots with minimum number of filled pixels which connect either vertically or horizontally or diagonally, all 9 neighbour equal, but never adding any additional "bold" connection? This is correct in Laegna number space.

Class is needed which gets image file folder+name, which can be relative from running directory, and it creates four png images automatically: black line on transparent (I), white line on transparent (E), black on white (O) and white on black (A), a relative disposition in Laegna Logecs -; it also creates U-variant which contains only the letter which is also the first letter of the number - E, O, A, I would be added before: "AE.png" becomes "E_AE.png", but for "AE.png" "U_AE.png" contains copy of "A_AE.png", while for "EE.png" the first letter is used to have "U_EE.png" is copy of "E_EE.png". This is the direction *encoded in number itself*, vs. the other cases where it's seen as connected to other value somehow, defined in local logic what is meant by this. So the folders last path, the directory name and everything connected is ignored, only the filename used and prefic added, and from one template filename from input, 5 filenames are generated; from same sequence of lines where color is not specified by drawer, each 4 styles is generated and the local favourite style is added, for example to show that number was presented in wrong domain, or falsely associated with it, depending on context and other symbols - this coloring only shows a very basic conflict or coherence, or automatic coherence in case of "U", or "unspecified". Because Laegna Logecs also supports "false spaces" from both ends.

So my use case:

laenumpng("AE.png", "subfolder/")

In subfolder, "I_AE", "O_AE", "U_AE", "A_AE", "E_AE" is generated, all five have ".png" suffix added to end, and "U_AE" is copy of A_AE" because both start with same letter, and U keeps the next letter.

Finally, "V_AE" should copy the *opposite* letter: O for A, A for O, I for E and E for I, so that the client could see also the yinyang kind of opposition space of these numbers and their separate dimensions.