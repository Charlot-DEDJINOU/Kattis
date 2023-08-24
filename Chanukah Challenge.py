n = int(input())

for _ in range(n) :
    a , b = map(int , input().split())
    ari = (1+b)*b//2
    print(a,b + ari)