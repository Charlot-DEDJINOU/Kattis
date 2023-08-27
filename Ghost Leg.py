n , m = map(int , input().split())
destination = [0]*n
barreau = []
for _ in range(m) :
    barreau.append(int(input()))

for i in range(1 , n+1) :
    s = i
    for x in barreau :
        if s == x :
            s = x + 1
        elif s == x + 1 :
            s = x
    
    destination[s-1] = i

print(*destination , sep='\n')
