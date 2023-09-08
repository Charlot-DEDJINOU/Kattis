carre = 1
points = 4
arretes = 4
n = int(input())
for _ in range(n) :
    points += arretes + carre
    carre *=4
    arretes = arretes * 2 + carre

print(points)