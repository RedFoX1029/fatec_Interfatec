n1, n2 = input().split()

n1 = int(n1)
n2 = int(n2)

if (n1 == n2):
    n3 = n1
elif (n1 > n2):
    n3 = n1
elif (n1 < n2):
    n3 = n2

print(n3)
