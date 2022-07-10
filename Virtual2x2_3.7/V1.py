
# The Virtual 2x2 Rubik's Cube Simulator!
# TL;DR Basically uses 6 lists to represent the faces of the cube and simulates turns by reordering the 24
# unique variables within and across each list.
#
# The list method used to simulate a turn on a Rubik's cube involves rotating the face that is turned
# (which is easily done by reordering the face's list so the last or x[3] is moved to the front)
# and rotating the 4 color pairs adjacent to the rotating face which is actually the more difficult part
# that involves two functions. One that copy the current adjacent pairs, and another that
# inserts the pair into it's new face's list while poping out the color pair it replaces.
# The two functions for the adjacent pairs account for more than 200 lines of code.
# That's mostly because there are six variations of those two functions for each of the faces.
# A goal for the v2 is to create a function (or set of functions) that can be applied to any face
# That would make it viable to create a 3x3 using the list format because it is really inefficient
# to create unique functions that essentially do the same thing
#
#
# Represents the 6 colors on four tiles in each face
# Orange doesn't use ansi code so it is only shown when ran in the terminal

A = B = C = D = "\033[37;1;47mWW\033[0m"            # White
E = F = G = H = "\033[32;1;42mGG\033[0m"            # Green
I = J = K = L = "\033[31;1;41mRR\033[0m"            # Red
M = N = O = P = "\033[34;1;44mBB\033[0m"            # Blue
Q = R = S = T = "\033[48;2;255;165;0mOO\033[0m"     # Orange
U = V = W = Z = "\033[33;1;43mYY\033[0m"            # Yellow

# Used for debugging:

#A = "W1"
#B = "W2"
#C = "W3"
#D = "W4"
#E = "G1"
#F = "G2"
#G = "G3"
#H = "G4"
#I = "R1"
#J = "R2"
#K = "R3"
#L = "R4"
#M = "B1"
#N = "B2"
#O = "B3"
#P = "B4"
#Q = "O1"
#R = "O2"
#S = "O3"
#T = "O4"
#U = "Y1"
#V = "Y2"
#W = "Y3"
#Z = "Y4"

# Represents each face of the cube.
# ***These lists are what the entire program reorders to simulate a turn***

WF = [A, B, C, D]
GF = [E, F, G, H]
RF = [I, J, K, L]
BF = [M, N, O, P]
OF = [Q, R, S, T]
YF = [U, V, W, Z]


# Prints the colors based on the order of how they appear on the list above that represents a face.

print("    " + WF[0] + WF[1])
print("    " + WF[3] + WF[2])
print(OF[0] + OF[1] + GF[0] + GF[1] + RF[0] + RF[1] + BF[0] + BF[1])
print(OF[3] + OF[2] + GF[3] + GF[2] + RF[3] + RF[2] + BF[3] + BF[2])
print("    " + YF[0] + YF[1])
print("    " + YF[3] + YF[2])

# Simulates the cube by printing out the list of each face.


def sim():
    print("")
    print("    " + WF[0] + WF[1])
    print("    " + WF[3] + WF[2])
    print(OF[0] + OF[1] + GF[0] + GF[1] + RF[0] + RF[1] + BF[0] + BF[1])
    print(OF[3] + OF[2] + GF[3] + GF[2] + RF[3] + RF[2] + BF[3] + BF[2])
    print("    " + YF[0] + YF[1])
    print("    " + YF[3] + YF[2])
    print("")


def rotate(x):
    x.insert(0, x[3])
    x.pop()


def intro():
    print("")
    print("The image above represents a 3D 2x2x2 Rubik's cube in 2D.")
    print("What makes it special is the ability to rotate any face.")
    print("However, rotating a face will affect the colors on adjacent faces.")
    print("For clockwise, type F,U,R,L,B,D")
    print("For anticlockwise type ' after the move")
    print("To simulate multiple consecutive moves, separate the letters with a space")

# Gives user information and turn notation.


intro()

# these temp lists temporairly store the 4 pairs of colors that are adjacent to x face
# that is being rotated


templ = []
tempu = []
tempr = []
tempd = []

# lurdcopy copies the pair to the left, up, right, and down of the face that is rotating
# by storing them in the temp lists

# F turn:


def zlurdcopy():

    templ.insert(0, OF[2])
    templ.insert(0, OF[1])

    tempu.insert(0, WF[2])
    tempu.insert(0, WF[3])

    tempr.insert(0, RF[0])
    tempr.insert(0, RF[3])

    tempd.insert(0, YF[1])
    tempd.insert(0, YF[0])

# lurdinsert inserts the copied pairs into the list of the new face the pair has moved to.
# The pair of colors that was there previously is popped out.


def zlurdinsert():

    WF.insert(2, templ[0])
    WF.insert(3, templ[1])
    WF.pop()
    WF.pop()

    RF.insert(0, tempu[0])
    RF.insert(-1, tempu[1])
    RF.pop(1)
    RF.pop(-1)

    YF.insert(2, tempr[0])
    YF.insert(3, tempr[1])
    YF.pop(0)
    YF.pop(0)

    OF.insert(1, tempd[0])
    OF.insert(2, tempd[1])
    OF.pop(-2)
    OF.pop(-2)

# R Turn:


def xlurdcopy():

    templ.insert(0, GF[2])
    templ.insert(0, GF[1])

    tempu.insert(0, WF[1])
    tempu.insert(0, WF[2])

    tempr.insert(0, BF[0])
    tempr.insert(0, BF[3])

    tempd.insert(0, YF[2])
    tempd.insert(0, YF[1])


def xlurdinsert():

    WF.insert(1, templ[0])
    WF.insert(2, templ[1])
    WF.pop(-2)
    WF.pop(-2)

    BF.insert(0, tempu[0])
    BF.insert(-1, tempu[1])
    BF.pop(1)
    BF.pop(-1)

    YF.insert(1, tempr[0])
    YF.insert(2, tempr[1])
    YF.pop(-2)
    YF.pop(-2)

    GF.insert(1, tempd[0])
    GF.insert(2, tempd[1])
    GF.pop(-2)
    GF.pop(-2)

# U Turn:


def ylurdcopy():

    templ.insert(0, OF[1])
    templ.insert(0, OF[0])

    tempu.insert(0, BF[0])
    tempu.insert(0, BF[1])

    tempr.insert(0, RF[1])
    tempr.insert(0, RF[0])

    tempd.insert(0, GF[0])
    tempd.insert(0, GF[1])


def ylurdinsert():

    BF.insert(2, templ[0])
    BF.insert(3, templ[1])
    BF.pop(0)
    BF.pop(0)

    RF.insert(0, tempu[0])
    RF.insert(0, tempu[1])
    RF.pop(-3)
    RF.pop(-3)

    GF.insert(2, tempr[0])
    GF.insert(3, tempr[1])
    GF.pop(0)
    GF.pop(0)

    OF.insert(0, tempd[0])
    OF.insert(0, tempd[1])
    OF.pop(-3)
    OF.pop(-3)

# B Turn:


def izlurdcopy():

    templ.insert(0, OF[0])
    templ.insert(0, OF[3])

    tempu.insert(0, YF[3])
    tempu.insert(0, YF[2])

    tempr.insert(0, RF[2])
    tempr.insert(0, RF[1])

    tempd.insert(0, WF[0])
    tempd.insert(0, WF[1])

def izlurdinsert():

    YF.insert(2, templ[0])
    YF.insert(3, templ[1])
    YF.pop()
    YF.pop()

    RF.insert(1, tempu[0])
    RF.insert(2, tempu[1])
    RF.pop(3)
    RF.pop(3)


    WF.insert(2, tempr[0])
    WF.insert(3, tempr[1])
    WF.pop(0)
    WF.pop(0)

    OF.insert(1, tempd[0])
    OF.insert(4, tempd[1])
    OF.pop(0)
    OF.pop(-1)

# L Turn:


def ixlurdcopy():

    templ.insert(0, BF[1])
    templ.insert(0, BF[2])

    tempu.insert(0, WF[3])
    tempu.insert(0, WF[0])

    tempr.insert(0, GF[3])
    tempr.insert(0, GF[0])

    tempd.insert(0, YF[3])
    tempd.insert(0, YF[0])


def ixlurdinsert():

    WF.insert(1, templ[0])
    WF.insert(4, templ[1])
    WF.pop(0)
    WF.pop()

    GF.insert(1, tempu[0])
    GF.insert(4, tempu[1])
    GF.pop(0)
    GF.pop()

    YF.insert(1, tempr[0])
    YF.insert(4, tempr[1])
    YF.pop(0)
    YF.pop()

    BF.insert(1, tempd[0])
    BF.insert(2, tempd[1])
    BF.pop(-2)
    BF.pop(-2)


# D Turn:


def iylurdcopy():

    templ.insert(0, OF[3])
    templ.insert(0, OF[2])

    tempu.insert(0, GF[3])
    tempu.insert(0, GF[2])

    tempr.insert(0, RF[3])
    tempr.insert(0, RF[2])

    tempd.insert(0, BF[3])
    tempd.insert(0, BF[2])


def iylurdinsert():

    GF.insert(2, templ[0])
    GF.insert(3, templ[1])
    GF.pop()
    GF.pop()

    RF.insert(2, tempu[0])
    RF.insert(3, tempu[1])
    RF.pop()
    RF.pop()

    BF.insert(2, tempr[0])
    BF.insert(3, tempr[1])
    BF.pop()
    BF.pop()

    OF.insert(2, tempd[0])
    OF.insert(3, tempd[1])
    OF.pop()

# lurddel is meant to delete the temporary lists so that it doesn't increase after every turn.


def lurddel():
    templ.pop()
    templ.pop()
    tempu.pop()
    tempu.pop()
    tempr.pop()
    tempr.pop()
    tempd.pop()
    tempd.pop()


def fturn():
    rotate(GF)
    zlurdcopy()
    zlurdinsert()
    lurddel()


def rturn():
    rotate(RF)
    xlurdcopy()
    xlurdinsert()
    lurddel()


def uturn():
    rotate(WF)
    ylurdcopy()
    ylurdinsert()
    lurddel()


def bturn():
    rotate(BF)
    izlurdcopy()
    izlurdinsert()
    lurddel()


def lturn():
    rotate(OF)
    ixlurdcopy()
    ixlurdinsert()
    lurddel()


def dturn():
    rotate(YF)
    iylurdcopy()
    iylurdinsert()
    lurddel()


def ifturn():
    fturn()
    fturn()
    fturn()


def irturn():
    rturn()
    rturn()
    rturn()


def iuturn():
    uturn()
    uturn()
    uturn()


def ibturn():
    bturn()
    bturn()
    bturn()


def ilturn():
    lturn()
    lturn()
    lturn()


def idturn():
    dturn()
    dturn()
    dturn()

# The main loop that executes functions based on the input. A recent improvement is using .split so that
# multiple moves can be simulated at once. This makes it possible to simulate any algorithm.


while True:
    print("")
    print("F-Front, U-Up, R-Right, L-Left, B-Back, D-Down, RESET-RESET")
    print("")
    move = input("Turn: ").upper()
    print(move)
    print()

    for i in move.split():
        if i == "F":
            fturn()
        if i == "R":
            rturn()
        if i == "U":
            uturn()
        if i == "B":
            bturn()
        if i == "L":
            lturn()
        if i == "D":
            dturn()
        if i == "F'":
            ifturn()
        if i == "R'":
            irturn()
        if i == "U'":
            iuturn()
        if i == "B'":
            ibturn()
        if i == "L'":
            irturn()
        if i == "D'":
            idturn()


        if i == "RESET":
            WF = [A, B, C, D]
            GF = [E, F, G, H]
            RF = [I, J, K, L]
            BF = [M, N, O, P]
            OF = [Q, R, S, T]
            YF = [U, V, W, Z]
            print("RESET")

    sim()
