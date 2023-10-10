p = int(input())
E = int(input())

people = dict()

for i in range(1 , p + 1) : people[i] = set()
for i in range(E) :
    p = list(map(int , input().split()[1:]))
    if 1 in p :
        for x in p : people[x].add(i)
    else :
        chansons = set()
        for x in p : 
            for j in people[x] :
                chansons.add(j)
        
        for x in p : people[x] = chansons.copy()
    
master = sorted(list(people[1]))
for key , value in people.items() :
    if master == sorted(list(value)) :
        print(key)