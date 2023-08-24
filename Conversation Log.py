n = int(input())
messages , allmessages , intersection = {} , [] , []

for _ in range(n) :
    s = input().split()
    if s[0] not in messages.keys() :
        messages[s[0]] = []
    
    messages[s[0]] += s[1:]
    allmessages += s[1:]

for value in messages.values() :
    if not intersection :
        intersection = value
    else :
        intersection = list(set(intersection) & set(value))
        if not intersection :
            break

if not intersection :
    print("ALL CLEAR")
else :
    repeat = {}
    for x in intersection :
       repeat[x] = allmessages.count(x)
    
    repeat = dict(sorted(repeat.items(), key=lambda item: (-item[1], item[0])))
    
    print(*repeat.keys(),sep='\n')