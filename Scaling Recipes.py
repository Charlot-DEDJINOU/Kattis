T = int(input())
ingedrients = []
poids = []
pourcentage = []
principal = 0

for _ in range(T):
    R,P,D = map(int , input().split())
    portion = D/P
    for x in range(R):
        s = input().split()
        ingedrients.append(s[0])
        poids.append(float(s[1]))
        pourcentage.append(float(s[2]))
        if(float(s[2]) == 100.0) :
            principal = float(s[1]) * portion
    
    print("Recipe #",_+1)
    for x in range(R) :
        print(ingedrients[x] , round(principal*pourcentage[x]/100,1), sep=" ")
    
    ingedrients = []
    poids = []
    pourcentage = []
    principal = 0

    print("-"*40)