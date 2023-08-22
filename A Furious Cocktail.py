n , t = map(int , input().split())
portions = []
for _ in range(n) :
    portions.append(int(input()))
portions = sorted(portions , reverse=True)

T = portions[0]
for i in range(1,n) :
    T = min(T-t , portions[i])
    if T <= 0 :
        break

if T <= 0 :
    print("NO")
else :
    print("YES")