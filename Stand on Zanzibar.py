n = int(input())
for _ in range(n) :
    s = list(map(int , input().split()))
    d = 0
    for i in range(1 , len(s)) :
        a , b = s[i] , s[i-1]
        d += a - b*2 if a > b*2 else 0
    
    print(d)
