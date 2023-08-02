s = []
while True :
    try :
        n = input().split()
        for _ in n :
            s.append(_)
    except EOFError:
        break

print(s)
"""
n = int(input())
h = input().split()
h = sorted([int(x) for x in h])
p = 2

for i in range(1,n+1) :
    if h[i-1] > i :
        p = 2
        break
    else :
        if p > h[i-1] / i :
            p = h[i-1] / i

if p == 2 :
    print("impossible")
else :
    print(round(p,1))
"""