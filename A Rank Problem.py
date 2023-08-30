n , m = map(int , input().split())
equipes = ['T'+str(i) for i in range(1 , n+1)]
for _ in range(m) :
    s = input().split()
    if equipes.index(s[0]) > equipes.index(s[1]) :
        equipes.remove(s[1])
        equipes.insert(equipes.index(s[0]) + 1 , s[1])

print(*equipes)