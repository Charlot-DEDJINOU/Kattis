n, m, a = int(input()), [], 0
for _ in range(n):
    m.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        if (m[i][j] - m[j][i]) % 2:
            print(-1)
            exit(0)
        a |= abs(m[i][j]) - abs(m[j][i])
if a:
    k1, k2 = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            k1[i][j] = k1[j][i] = (m[i][j] + m[j][i]) // 2
            k2[i][j], k2[j][i] = m[i][j] - k1[i][j], m[j][i] - k1[i][j]
    print(2)
    for r in k1:
        print(*r)
    for r in k2:
        print(*r)
else:
    print(1)
    for r in m:
        print(*r)
