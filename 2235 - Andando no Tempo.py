A, B , C = input(). split()

A= int(A)
B= int(B)
C= int(C)

if ( A == B or A == C or B == C or A + B == C or A == B +C or A + C == B):
    print("S")

else:
    print("N")
