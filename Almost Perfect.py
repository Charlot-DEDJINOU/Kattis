import math

def parfait(n):
    somme, i = 0, 1
    sqrt_n = int(math.sqrt(n)) + 1

    while i <= sqrt_n and i < n :
        if n % i == 0 :
            somme += i
            if i != 1 and i**2 != n :
                somme += n // i
            if somme == n:
                return "perfect"
            elif abs(somme - n) <= 2:
                return "almost perfect"
            elif somme > n:
                return "not perfect"
        
        i += 1
    return "not perfect"

while True:
    try:
        n = int(input())
        print(n, parfait(n))
    except EOFError:
        break
