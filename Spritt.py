x, n = map(int , input().split())
find = True

for _ in range(x) :
    n = n - int(input())
    if n < 0 :
        print('Neibb')
        find = False
        break

if find :
    print('Jebb')