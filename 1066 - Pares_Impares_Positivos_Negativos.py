n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0
if (n1 % 2) == 0:
    par = par + 1
    if (n1 > 0):
        positivo = positivo + 1
    elif (n1 < 0):
        negativo = negativo + 1
else:
    impar = impar + 1
    if (n1 > 0):
        positivo = positivo + 1
    elif (n1 < 0):
        negativo = negativo + 1

if (n2 % 2) == 0:
    par = par + 1
    if (n2 > 0):
        positivo = positivo + 1
    elif (n2 < 0):
        negativo = negativo + 1
else:
    impar = impar + 1
    if (n2 > 0):
        positivo = positivo + 1
    elif (n2 < 0):
        negativo = negativo + 1

if (n3 % 2) == 0:
    par = par + 1
    if (n3 > 0):
        positivo = positivo + 1
    elif (n3 < 0):
        negativo = negativo + 1
else:
    impar = impar + 1
    if (n3 > 0):
        positivo = positivo + 1
    elif (n3 < 0):
        negativo = negativo + 1

if (n4 % 2) == 0:
    par = par + 1
    if (n4 > 0):
        positivo = positivo + 1
    elif (n4 < 0):
        negativo = negativo + 1
else:
    impar = impar + 1
    if (n4 > 0):
        positivo = positivo + 1
    elif (n4 < 0):
        negativo = negativo + 1

if (n5 % 2) == 0:
    par = par + 1
    if (n5 > 0):
        positivo = positivo + 1
    elif (n5 < 0):
        negativo = negativo + 1
else:
    impar = impar + 1
    if (n5 > 0):
        positivo = positivo + 1
    elif (n5 < 0):
        negativo = negativo + 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")