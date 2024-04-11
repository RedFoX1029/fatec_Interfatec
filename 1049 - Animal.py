p1 = str(input())
p2 = str(input())
p3 = str(input())

if (p1 == "vertebrado"):
    if (p2 == "ave"):
        if (p3 == "carnivoro"):
            print("aguia")
        else:
            print("pomba")

    if (p2 == "mamifero"):
        if (p3 == "onivoro"):
            print("homem")
        else:
            print("vaca")
else:
    if (p2 == "inseto"):
        if (p3 == "hemafago"):
            print("pulga")
        else:
            print("lagarta")

    if (p2 == "anelideo"):
        if (p3 == "hemafago"):
            print("sanguessuga")
        else:
            print("minhoca")