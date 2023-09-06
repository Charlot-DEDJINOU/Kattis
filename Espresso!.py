n , s = map(int , input().split())
p , disponible = 0 , s
for _ in range(n) :
    etudiant = input().strip()
    quantity = 0
    if etudiant[-1] == 'L' :
        etudiant = etudiant[0]
        quantity = 1
    
    quantity += int(etudiant)

    if quantity > disponible :
        disponible = s
        p += 1

    disponible -= quantity

print(p)