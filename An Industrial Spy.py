from math import sqrt , floor
from itertools import permutations

def premier(n) :
    iteration , i = floor(sqrt(n)) , 2
    
    while i <= iteration :
        if n % i == 0 :
            return False
        
        i += 1
    
    return True

for _ in range(int(input())) :
    n = input().strip()
    total ,  yet = 0 , [0 , 1]
    for i in range(1 , len(n) + 1) :
        all_permutations = list(permutations(n , i))
        for x in all_permutations :
            x = int("".join(x))
            if x not in yet and premier(x) :
                total += 1
                yet.append(x)

    print(total)