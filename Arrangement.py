def drawn(s) :
    print('*'*s)

n = int(input())
m = int(input())

if m <= n :
    for _ in range(m) :
        drawn(1)
else :
    s = [m // n]*n
    q = m % n
    for i in range(q) :
        s[i] += 1

    for i in s :
        drawn(i)