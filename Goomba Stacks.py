gtotal = 0
possible = True
for _ in range(int(input())) :
    g , i = map(int , input().split())
    gtotal += g
    if gtotal < i :
        print("impossible")
        possible = False
        break

if possible == True :
    print("possible")