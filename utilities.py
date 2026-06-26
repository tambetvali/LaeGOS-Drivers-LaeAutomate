# This file contains small utilities and thus, only small contextual comments.

# It utilizes number system of SC1 you can convert with SC3.

import math

def generate_binary_numbers(R):
  """
  Generates binary numbers of length R using a functional approach.

  Args:
    R: The desired length of the binary numbers.

  Yields:
    Arrays of strings representing binary numbers (e.g., ['001', '010', 
'100', ...]).
  """
  if R == 0:
    yield []  # Base case: length 0
    return

  for i in range(2):  # Iterate through 0 and 1 for each digit
    for sub_list in generate_binary_numbers(R - 1):
      yield [str(i),] + sub_list

def R(_R = 0.5):
    if _R == 0:
        yield []
        return
    
    # Convert to binary digits
    _R = math.floor(_R * 2)
    for n in generate_binary_numbers(_R):
        for d in range(len(n)):
            if n[d] == '0': n[d] = "O"
            elif n[d] == '1': n[d] = "A"
        yield laenum(n)

# Create Json chapter "Axes" from it's self.axes, the first one.
class Laeaxes:
    def __init__(self):
        self.regaxe = {}
        self.axes = {}

        self.axes["UnSignedTen"] = {}
        self.axes["SignedTen"] = {}
        self.axes["UnSignedDec"] = {}
        self.axes["SignedDec"] = {}

    def findpoint(self, num):
        if num in self.regaxe:
            return
        self.regaxe[num] = True

        number = 0
        for laen in R(num):
            self.axes["UnSignedTen"][str(laen)] = laen.getUnSignedTen()
            self.axes["SignedTen"][str(laen)] = laen.getSignedTen()
            self.axes["UnSignedDec"][str(laen)] = laen.getUnSignedDec()
            self.axes["SignedDec"][str(laen)] = laen.getSignedDec()

    def UnSignedAxeLaeY(self, num, point):
        self.findpoint(num)
        return self.axes["UnSignedTen"][point]

    def SignedAxeLaeY(self, num, point):
        self.findpoint(num)
        return self.axes["SignedTen"][point]

    def UnSignedAxeDecY(self, num, point):
        self.findpoint(num)
        return self.axes["UnSignedDec"][point]

    def SignedAxeDecY(self, num, point):
        self.findpoint(num)
        return self.axes["SignedDec"][point]

    def SignedAxeTenYstr(self, num):
        self.findpoint(num)
        return "Axes.SignedTen[\"" + str(num) + "\"]"

    def UnSignedAxeTenYstr(self, num):
        self.findpoint(num)
        return "Axes.UnSignedTen[\"" + str(num) + "\"]"

    def SignedAxeDecYstr(self, num):
        self.findpoint(num)
        return "Axes.SignedDec[\"" + str(num) + "\"]"

    def UnSignedAxeDecYstr(self, num):
        self.findpoint(num)
        return "Axes.UnSignedDec[\"" + str(num) + "\"]"

    def SignedAxeTenYpnt(self, num, point):
        self.findpoint(num)
        return "Axes.SignedTen[\"" + str(num) + "\"][\"" + str(point) + "\"]"

    def UnSignedAxeTenYpnt(self, num, point):
        self.findpoint(num)
        return "Axes.UnSignedTen[\"" + str(num) + "\"][\"" + str(point) + "\"]"

    def SignedAxeDecYpnt(self, num, point):
        self.findpoint(num)
        return "Axes.SignedDec[\"" + str(num) + "\"][\"" + str(point) + "\"]"

    def UnSignedAxeDecYpnt(self, num, point):
        self.findpoint(num)
        return "Axes.UnSignedDec[\"" + str(num) + "\"][\"" + str(point) + "\"]"

# Growing singleton
laeaxes = Laeaxes()

class laerange:
    def __init__(self, R, sign = False):
        self.R = R
        self.sign = sign
        self.range = {}

    def setSize(self, vartype, size, sign = False):
        self.range = (size, size)

class Laeranges:
    def __init__(self):
        self.ranges = {}

    def setUpR(self, R):
        if R not in self.ranges:
            rang = {}
          
            rng = laerange(R)
            rng.setSize("SignedTen", 2**(R), True)
            rang["SignedTen"] = rng

            rng = laerange(R)
            rng.setSize("UnSignedTen", 2**(R + 1), False)
            rang["UnSignedTen"] = rng

            rng = laerange(R)
            rng.setSize("UnSignedDec", 2**(R), True)
            rang["UnSignedDec"] = rng

            rng = laerange(R)
            rng.setSize("SignedDec", 2**(R + 1), False)
            rang["SignedDec"] = rng

            self.ranges[R] = rang

    def UnSignedTen(self, R):
        if R not in self.ranges:
            self.setUpR(R)

        return self.ranges[R]["UnSignedTen"]

    def SignedTen(self, R):
        if R not in self.ranges:
            self.setUpR(R)

        return self.ranges[R]["SignedTen"]

    def UnSignedDec(self, R):
        if R not in self.ranges:
            self.setUpR(R)

        return self.ranges[R]["UnSignedDec"]

    def SignedDec(self, R):
        if R not in self.ranges:
            self.setUpR(R)

        return self.ranges[R]["SignedDec"]

# Growing singleton
laeranges = Laeranges()

# Create chapters for R's, subchapters for numbers.
class laenum:
    def __init__(self, digits = []):
        self.digits = digits
        self.axes = laeaxes

    # Let's call Laegna digit "ten"
    def addDigit(self, ten):
        self.digits.append(ten)

    def iterBaselae4(self):
        if self.digits == []:
            return
        
        n = ""
        for d in self.digits:
            n = n + d
            if len(n) == 2:
                if n == "AA": yield "E"
                if n == "AO": yield "A"
                if n == "OA": yield "O"
                if n == "OO": yield "I"
                n = ""
        # Could be averages of "A?" and "O?", intermediate points,
        # but this one suits R = 0.5 which we have as odd R here,
        # almost emulated but binary-safe.
        if n == "A": yield "E"
        if n == "O": yield "I"

    def Lae4(self):
      num = ""
      for d in self.iterBaselae4():
        num += d
      return num

    def LaeComplex(self):
        digitval1 = ""
        digitval2 = ""
        for digit in self.iterBaselae4():
            if digit == 'I':
              digitval1 += 'O'
              digitval2 += 'O'
            if digit == 'O':
              digitval1 += 'O'
              digitval2 += 'A'
            if digit == 'A':
              digitval1 += 'A'
              digitval2 += 'O'
            if digit == 'E':
              digitval1 += 'A'
              digitval2 += 'A'
        digits = digitval1 + digitval2
        numb = laenum(digits)
        digits = laenum(digits).Lae4()
        return digits

    def iterLaeComplex(self):
        if self.digits == []:
            return
        
        for d in self.LaeComplex():
            yield d

    def iterBaselae4conc(self):
        full = ""
        for n in self.iterBaselae4():
            full = full + n
            yield full

    def __str__(self):
        laenum = ""
        for d in self.iterBaselae4():
            laenum += d
        return laenum

    # Return single digit of given Laegna number
    def __getitem__(self, d):
        return self.digits[d]

    def getUnSignedTen(self):
        decimal_value = 0
        power = len(self.digits) // 2
        for digit in self.iterBaselae4():
            if digit == 'I': digitval = 0
            if digit == 'O': digitval = 1
            if digit == 'A': digitval = 2
            if digit == 'E': digitval = 3
            decimal_value += digitval * 4**(power - 1)
            power -= 1
        decimal_value = decimal_value + 1
        return decimal_value

    def getSignedTen(self):
        decimal_value = self.getUnSignedTen() - 4**((len(self.digits) // 2)) // 2
        if decimal_value < 1: decimal_value = decimal_value - 1
        return decimal_value

    def getUnSignedDec(self):
        decimal_value = 0
        power = len(self.digits) // 2
        for digit in self.iterLaeComplex():
            if digit == 'I': digitval = 0
            if digit == 'O': digitval = 1
            if digit == 'A': digitval = 2
            if digit == 'E': digitval = 3
            decimal_value += digitval * 4**(power - 1)
            power -= 1
        decimal_value = decimal_value + 1
        return decimal_value

    def getSignedDec(self):
        decimal_value = self.getUnSignedDec() - 4**((len(self.digits) // 2)) // 2
        if decimal_value < 1: decimal_value = decimal_value - 1
        return decimal_value

    def getR(self):
        R = len(self.digits) * 0.5
        if R == math.floor(R): R = math.floor(R)
        
        return R

    def generatePoints(self):
        num = 0
        points = {}

        for point in self.iterBaselae4conc():
            Point = {}
            num = num + 1

            Point["R"] = self.getR()

            # Initialization of variables
            Point["Ten"] = {}
            Point["Id"] = num
            Point["Ten"]["Signed"] = {}
            Point["Ten"]["Signed"]["SrcAxeY"] = self.axes.SignedAxeTenYstr(num)
            Point["Ten"]["Signed"]["SrcY"] = self.axes.SignedAxeTenYpnt(num, point)
            Point["Ten"]["Signed"]["X"] = 4**(num - 0.5)
            Point["Ten"]["Signed"]["Y"] = self.axes.SignedAxeLaeY(num, point)
            Point["Ten"]["UnSigned"] = {}
            Point["Ten"]["UnSigned"]["SrcAxeY"] = self.axes.UnSignedAxeTenYstr(num)
            Point["Ten"]["UnSigned"]["SrcY"] = self.axes.UnSignedAxeTenYpnt(num, point)
            Point["Ten"]["UnSigned"]["X"] = 4**(num)
            Point["Ten"]["UnSigned"]["Y"] = self.axes.UnSignedAxeLaeY(num, point)
            Point["Dec"] = {}
            Point["Dec"]["Signed"] = {}
            Point["Dec"]["Signed"]["SrcAxeY"] = self.axes.SignedAxeDecYstr(num)
            Point["Dec"]["Signed"]["SrcY"] = self.axes.SignedAxeDecYpnt(num, point)
            Point["Dec"]["Signed"]["X"] = 4**(num - 0.5)
            Point["Dec"]["Signed"]["Y"] = self.axes.SignedAxeDecY(num, point)
            Point["Dec"]["UnSigned"] = {}
            Point["Dec"]["UnSigned"]["SrcAxeY"] = self.axes.UnSignedAxeDecYstr(num)
            Point["Dec"]["UnSigned"]["SrcY"] = self.axes.UnSignedAxeDecYpnt(num, point)
            Point["Dec"]["UnSigned"]["X"] = 4**(num)
            Point["Dec"]["UnSigned"]["Y"] = self.axes.UnSignedAxeDecY(num, point)

            points[Point["Id"]] = Point

        return points

class laenumCanvas:
    def __init__(self, laen):
        self.laen = laen

        # cd - Canvas Draw
        self.CD = {}

        self.CD["SignedTen"] = {}
        self.CD["SignedTen"]["Range"] = laeranges.SignedTen(self.laen.getR())
        self.draw("Signed", "Ten")

        self.CD["UnSignedTen"] = {}
        self.CD["UnSignedTen"]["Range"] = laeranges.UnSignedTen(self.laen.getR())
        self.draw("UnSigned", "Ten")

        self.CD["SignedDec"] = {}
        self.CD["SignedDec"]["Range"] = laeranges.SignedDec(self.laen.getR())
        self.draw("Signed", "Dec")

        self.CD["UnSignedDec"] = {}
        self.CD["UnSignedDec"]["Range"] = laeranges.UnSignedDec(self.laen.getR())
        self.draw("UnSigned", "Dec")

    def draw(self, s, t):
        CD = self.CD[s + t]
        points = self.laen.generatePoints()

        
