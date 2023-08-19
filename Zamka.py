L = int(input())
D = int(input())
X = int(input())
res = []
for i in range(L,D + 1) :
    if sum([int(x) for x in str(i)]) == X :
        res.append(i)

print(min(res))
print(max(res))