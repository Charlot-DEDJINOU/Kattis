n ,k = map(int , input().split())
s = list(map(int , input().split()))

if k == 1 :
    print(*s)
else :
    for i in range(k - 1 , n , k) :
        print(s[i],end=' ')