from collections import Counter

n, b = map(int, input().split())
tab = []

for _ in range(b):
    tab.append(int(input()))

print(*[x for x in range(n) if x not in tab] , sep='\n')
print("Mario got", len(Counter(tab)), "of the dangerous obstacles.")