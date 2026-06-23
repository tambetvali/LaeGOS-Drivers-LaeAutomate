# Laegna Source Database files => AI ***Plug'n'Play*** / Robot-Module *uses* ****JSON api***.

These files are intented to be applied as primary, compatible database of Laegna Numbers in projects which use them and need basic data verification.

Three systems of Laegna are covered here, where html files can be used to understand how to create drivers (English explanations), and decoder.py explains the internal structure, invariant for longer digit-lengths (bigger R):
- ZXY system base-3
- IOAE laegna system base-4
- IOAE laegna wave system base-4
- Letters represent digits:

Finite coordinate system scoping:

Z = -1 (1st diff); X = 0 (linear); Y = 1 (first exp).

I = -2 (minus exp); O = -1 (minus linear); A = 1 (plus linear); E = 2 (plus exp).

I, E: log-exp scale 1/2 + 1/2 (two half ranges).

O, A: linear scale 1 (one full range).

And here, understanding of it's structure starts from...
