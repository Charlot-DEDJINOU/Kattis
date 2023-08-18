n = int(input())
distance = []
temps = []
vitesse = 0
for _ in range(n) :
    t , d = map(int , input().split())   
    if distance :
        new_vitesse = (d - distance[-1]) / (t - temps[-1])
        vitesse = max(vitesse , new_vitesse)
    
    distance.append(d)
    temps.append(t)

print(int(vitesse))
