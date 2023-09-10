n = int(input())
dom = dict()
total = 0

for _ in range(n) :
    s = input()
    if s in dom.keys() :
        dom[s] += 1
    else :
        dom[s] = 1

for _ in range(n) :
    s = input()
    if s in dom.keys() and dom[s] > 0 :
        total += 1
        dom[s] -=1

print(total)