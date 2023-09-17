p = int(input())
tab = []

for _ in range(p):
    a, b, n = map(int, input().split())
    total = 0
    while n >= b:
        total += (n % b) ** 2
        n //= b
    total += n ** 2
    tab.append(total)

for i, value in enumerate(tab):
    print(f"{i + 1} {value}")