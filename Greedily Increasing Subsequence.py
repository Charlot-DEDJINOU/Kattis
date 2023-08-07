n = int(input())
s = list(map(int, input().split()))
gic = []

for x in s:
    if not gic or x > gic[-1]:
        gic.append(x)

print(len(gic))
print(*gic)