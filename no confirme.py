n, p = map(int, input().split())
pairs , joueurs = {} , []
number_pairs = 0

def together(old, s):
    if old[0] != s[0] and s[0] not in pairs[old[0]] and old[0] not in pairs[s[0]]:
        diff_x = s[1] - old[1]
        diff_y = s[2] - old[2]
        diff_t = abs(s[3] - old[3])
        
        distance = (diff_x**2 + diff_y**2)**0.5
        temps = diff_t
    
        return distance <= 1000 and temps <= 10
    
    return False

for _ in range(p):
    s = list(map(int, input().split()))
    joueurs.append(s)

    if s[0] not in pairs.keys():
        pairs[s[0]] = set()

    for i in range(len(joueurs) - 1):
        if together(joueurs[i], s):
            pairs[joueurs[i][0]].add(s[0])
            number_pairs += 1

print(number_pairs)
for key, value in list(sorted(pairs.items())):
    for v in value:
        print(key, v)

from math import cos , sin , acos
R = 6371009
for _ in range(int(input())) :
    lat1 , lon1 , lat2 , lon2 = map(float, input().split())
    s = acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon1-lon2))
    d = s * R
    print(s-d)