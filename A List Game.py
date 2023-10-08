def generer_nombres_premiers(n):
    premiers = [True] * (n + 1)
    premiers[0] = premiers[1] = False
    for i in range(2, int(n**0.5) + 1):
        if premiers[i]:
            for j in range(i*i, n+1, i):
                premiers[j] = False
    return [i for i in range(2, n+1) if premiers[i]]

def decomposer_en_premiers_optimise(n):
    total = 0
    nombres_premiers = generer_nombres_premiers(int(n**0.5) + 1)
    
    for diviseur in nombres_premiers:
        while n % diviseur == 0:
            total += 1
            n //= diviseur
    
    if n > 1:
         total += 1
    
    return  total

nombre = int(input())
resultat = decomposer_en_premiers_optimise(nombre)
print(resultat)
