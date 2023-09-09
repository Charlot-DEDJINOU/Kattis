r , c , zr , zc = map(int , input().split())
matrix = []
for i in range(r) :
    s = input()
    s = [x*zc for x in s]
    for _ in range(zr) :
        print(*s , sep="")