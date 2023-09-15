from collections import Counter

p , t = map(int , input().split())
pair = dict()

try :
    for _ in range(p*t) :
        pe , tr = map(int , input().split())
        if pe in pair.keys() :
            pair[pe].append(tr)
        else :
            pair[pe] = [tr]

except EOFError :
    pass

unique_opinions = set()

for opinion in pair.values():
    unique_opinions.add(tuple(sorted(opinion)))  

res = len(unique_opinions) 
res += 1 if p > len(pair) else 0

print(res)