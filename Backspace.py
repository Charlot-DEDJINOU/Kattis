s = input()
res = []
for x in s :
    if x == "<" :
        a = res.pop()
    else :
        res.append(x)

print("".join(res))