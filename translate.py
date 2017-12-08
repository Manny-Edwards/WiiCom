from wiimote import getTranslation, receive_translations
import requests

translated = []
A = ["dot", "dash"]
B = ["dash", "dot", "dot", "dot"]
C = ["dash", "dot", "dash", "dot"]
D = ["dash", "dot", "dot"]
E = ["dot"]
F = ["dot", "dot", "dash", "dot"]
G = ["dash", "dash", "dot"]
H = ["dot", "dot", "dot", "dot"]
I = ["dot", "dot"]
J = ["dot", "dash", "dash", "dash"]
K = ["dash", "dot", "dash"]
L = ["dot", "dash", "dot", "dot"]
M = ["dash", "dash"]
N = ["dash", "dot"]
O = ["dash", "dash", "dash"]
P = ["dot", "dash", "dash", "dot"]
Q = ["dash", "dash", "dot", "dash"]
R = ["dot", "dash", "dot"]
S = ["dot", "dot", "dot"]
T = ["dash"]
U = ["dot", "dot", "dash"]
V = ["dot", "dot", "dot", "dash"]
W = ["dot", "dash", "dash"]
X = ["dash", "dot", "dot", "dash"]
Y = ["dash", "dot", "dash", "dash"]
Z = ["dash", "dash", "dot", "dot"]


def trans_to_eng():
    translations = getTranslation()
    for letters in translations:
        if letters == (A):
            translated.append("A")
        if letters == (B):
            translated.append("B")
        if letters == (C):
            translated.append("C")
        if letters == (D):
            translated.append("D")
        if letters == (E):
            translated.append("E")
        if letters == (F):
            translated.append("F")
        if letters == (G):
            translated.append("G")
        if letters == (H):
            translated.append("H")
        if letters == (I):
            translated.append("I")
        if letters == (J):
            translated.append("J")
        if letters == (K):
            translated.append("K")
        if letters == (L):
            translated.append("L")
        if letters == (M):
            translated.append("M")
        if letters == (N):
            translated.append("N")
        if letters == (O):
            translated.append("O")
        if letters == (P):
            translated.append("P")
        if letters == (Q):
            translated.append("Q")
        if letters == (R):
            translated.append("R")
        if letters == (S):
            translated.append("S")
        if letters == (T):
            translated.append("T")
        if letters == (U):
            translated.append("U")
        if letters == (V):
            translated.append("V")
        if letters == (W):
            translated.append("W")
        if letters == (X):
            translated.append("X")
        if letters == (Y):
            translated.append("Y")
        if letters == (Z):
            translated.append("Z")
        word = ""
        for x in translated:
            word += x
    print(word + " will be sent.")
    return word


def trans_to_code(word):
    for letters in word:
        if letters == ("A"):
            translated.append(A)
        if letters == ("B"):
            translated.append(B)
        if letters == ("C"):
            translated.append(C)
        if letters == ("D"):
            translated.append(D)
        if letters == ("E"):
            translated.append(E)
        if letters == ("F"):
            translated.append(F)
        if letters == ("G"):
            translated.append(G)
        if letters == ("H"):
            translated.append(H)
        if letters == ("I"):
            translated.append(I)
        if letters == ("J"):
            translated.append(J)
        if letters == ("K"):
            translated.append(K)
        if letters == ("L"):
            translated.append(L)
        if letters == ("M"):
            translated.append(M)
        if letters == ("N"):
            translated.append(N)
        if letters == ("O"):
            translated.append(O)
        if letters == ("P"):
            translated.append(P)
        if letters == ("Q"):
            translated.append(Q)
        if letters == ("R"):
            translated.append(R)
        if letters == ("S"):
            translated.append(S)
        if letters == ("T"):
            translated.append(T)
        if letters == ("U"):
            translated.append(U)
        if letters == ("V"):
            translated.append(V)
        if letters == ("W"):
            translated.append(W)
        if letters == ("X"):
            translated.append(X)
        if letters == ("Y"):
            translated.append(Y)
        if letters == ("Z"):
            translated.append(Z)
    receive_translations(translated)
