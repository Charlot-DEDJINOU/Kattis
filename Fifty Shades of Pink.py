n = int(input())
count = 0
for _ in range(n) :
    s = input().lower()
    if 'rose' in s or 'pink' in s : count +=1

if count :
    print(count)
else :
    print("I must watch Star Wars with my daughter")