tour = int(input())
cont = 1
words=[]
for i in range(tour) :
    mots=input().split(" ")
    phrases=[]
    cont = 1
    while cont == 1 :
        phase=input()
        if phase == "what does the fox say?" :
            phase=[]
            cont = 0
            continue
        else :
            phrases=set(phase.split(" ")) | set(phrases)
    for mot in mots :
        if mot not in phrases :
            phase.append(mot)
    words.append(phase)

for res in words :
    for i in res :
        print(i,end=" ")
    print("")