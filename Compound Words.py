from itertools import combinations

words = []

try :
    while True:
        s = input().split()
        
        for word in s:
            words.append(word)
except EOFError :
    pass

word_combinations = combinations(words, 2)
word_composite = []

for x in word_combinations :
    word_composite.append([x[1] , x[0]])
    word_composite.append([x[0] , x[1]])

word_composite = sorted(set(["".join(x) for x in word_composite]))

print(*word_composite,sep='\n')