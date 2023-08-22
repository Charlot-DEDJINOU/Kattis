n = int(input())
s = []
for _ in range(n) :
    s.append(int(input()))

s.sort(reverse=True)
print(sum([s[i] for i in range(n) if i % 3 != 2]))