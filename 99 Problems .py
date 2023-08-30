from sys import stdin

n , q = map(int , stdin.readline().split())
n = list(map(int , stdin.readline().split()))
for _ in range(q) :
    s = list(map(int , stdin.readline().split()))
    found = False
    if s[0] == 1 :
        for index , value in enumerate(n) :
            if value > s[1] :
                found = True
                print(n.pop(index))
                break
    else :
        for index , value in enumerate(n) :
            if value <= s[1] :
                found = True
                print(n.pop(index))
                break
    
    if not found :
        print(-1)