n , m , k = list(map(int ,input().split()))
etudiants = list()
classe = dict()

for _ in range(n) :
    etudiants.append(input())

for i in range(k) :
    classe[chr(65 + i)] = -1

i = 0
yet_color = []
while i < m and -1 in classe.values() :
    col , j = [] , 0
    while j < n and len(col) <= k :
        if etudiants[j][i] not in col :
            col.append(etudiants[j][i])

        j += 1

    inter = [x for x in yet_color if x in col]
    if inter :
        y = classe[inter[0]]
    else :
        y = i
    
    for x in col :
        classe[x] = y
        yet_color.append(x)

    i += 1

print(len(set(classe.values())))