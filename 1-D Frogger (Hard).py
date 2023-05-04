def charlot(tab, index, case_magic):
    if 0 <= index < len(tab) and tab[index] != 0:
        tmp = tab[index]
        tab[index] = 0
        return tmp == case_magic or charlot(tab, index + tmp, case_magic)
    return False

n = int(input())
s = [int(x) for x in input().split()]
instance = 0
for i in range(n):
    for j in range(n):
        if i == j or charlot(s[:], i, s[j]):
            instance += 1
print(instance)
