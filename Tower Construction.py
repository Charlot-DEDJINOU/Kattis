n = int(input())
briques = list(map(int , input().split()))
total = 1
for i in range(1,n) :
    if briques[i] > briques[i-1] :
        total += 1

print(total)