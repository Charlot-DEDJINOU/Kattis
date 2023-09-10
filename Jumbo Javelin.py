n = int(input())
somme = 0
for _ in range(n) :
    somme += int(input())

print(somme - (n - 1))