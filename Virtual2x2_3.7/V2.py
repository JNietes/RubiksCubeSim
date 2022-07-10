# The purpose is to try to create a function or set of functions that simulate a turn AND can be applied
# to any of the faces. Theoretically this format can be tweaked to create virtual a 3x3 and possibly 4x4s
# although for a 4x4 the inner layers would involve a somewhat different function. It won't be as complicated
# as turning a face though.

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
J = "J"
K = "K"
L = "L"
M = "M"
N = "N"
O = "O"
P = "P"
Q = "Q"
R = "R"
S = "S"
T = "T"
U = "U"
V = "V"
W = "W"
Z = "Z"
X = "XX"    # a placeholder variable


OL = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, Z]
ML = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, Z]
FF = [[E, F, G, H], [S, D, I, V], [R, C, L, U]]
print("Before ML: ", ML)
print("Before OL: ", OL)
print("Before FF: ", FF)
def turn(face):
    # face rotation
    i = OL.index(face[0][0])
    ii = OL.index(face[0][3])
    ML.insert(i, face[0][3]), ML.pop(ii + 1)

    i = OL.index(face[0][1])
    ii = OL.index(face[0][0])
    ML.insert(i, face[0][0]), ML.pop(ii + 1)

    i = OL.index(face[0][2])
    ii = OL.index(face[0][1])
    ML.insert(i, face[0][1]), ML.pop(ii + 1)

    i = OL.index(face[0][3])
    ii = OL.index(face[0][2])
    ML.insert(i, face[0][2]), ML.pop(ii + 1)

    OL.clear()
    OL.extend(ML)

    # first set of pairs
    i = OL.index(face[1][0])
    ii = OL.index(face[1][3])
    ML.insert(i, face[1][3]), ML.pop(ii + 1)

    i = OL.index(face[1][1])
    ii = OL.index(face[1][0])
    ML.insert(i, face[1][0]), ML.pop(ii + 1)
    print("After OL:  ", OL)
    OL.clear()
    OL.extend(ML)




turn(FF)
print("After ML:  ", ML)


