n = int(input())
somme = 0
for _ in range(n) :
    s = input()
    power = int(s[-1])
    nombre = int(s[:-1])
    somme +=pow(nombre , power)

print(somme)