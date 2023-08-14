n , m = map(int , input().split())
s = list(map(int , input().split()))
count = 0
for i in range(n-m+1) :
    if sum([1 for x in range(m) if s[i+x]%2 == 0]) > 1 :
        count += 1
print(count)