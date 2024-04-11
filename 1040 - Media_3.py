n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

m1 = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

if (m1 >= 7):
    print(f"Media: {m1:.1f}")
    print("Aluno aprovado.")
elif (m1 < 5):
    print(f"Media: {m1:.1f}")
    print("Aluno reprovado.")
elif (m1 >= 5 and m1 <= 6.9):
    n5 = float(input())
    m2 = (n5 + m1) / 2

    if (m2 > 5):
        print(f"Media: {m1:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {n5:.1f}")
        print("Aluno aprovado.")
        print(f"Media final: {m2:.1f}")
    elif (m2 < 4.9):
        print(f"Media: {m1:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {n5:.1f}")
        print("Aluno reprovado.")
        print(f"Media final: {m2:.1f}")