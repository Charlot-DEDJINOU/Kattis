gobelet = dict()
for _ in range(int(input())) :
    s = input().split()
    radius , color = 0 , ""
    try :
        radius = int(s[1])
        color = s[0]
    except :
        radius = int(s[0]) // 2
        color = s[1]
    
    gobelet[color] = radius

gobelet = dict(sorted(gobelet.items() , key = lambda item : (item[1] , item[0])))

print(*gobelet.keys(),sep='\n')