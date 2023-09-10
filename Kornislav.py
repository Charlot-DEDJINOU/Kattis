from itertools import permutations
s = list(map(int , input().split()))
op_permutations = list(permutations(s))
maxi = 0
for s in op_permutations :
    if s[0] >= s[2] and s[3] >= s[1] :
        maxi = max(maxi , s[2] * s[1])

print(maxi)