n = int(input())
somme = 0
for _ in range(n):
    a, b = map(float, input().split())
    somme += a * b

print(somme)
