n = int(input())
t = []
start = 0
for _ in range(n) :
    a , b = map(int , input().split())
    s = [x for x in range(a,b+1)]
    if start == 0 :
        start = 1
        t = s
    else :
        t = [x for x in t if x in s]

if len(t) != 0 :
    print("gunilla has a point")
else :
    print("edward is right")