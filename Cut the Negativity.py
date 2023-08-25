n = int(input())
possible = list()
for i in range(1 , n+1) :
    s = list(map(int , input().split()))
    for j in range(1 , n+1) :
        if s[j-1] != -1 :
            possible.append([i , j , s[j-1]])

print(len(possible))
for item in possible :
    print(*item)