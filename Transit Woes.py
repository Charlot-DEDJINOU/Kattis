def attente(a , b) :
    if a <= b :
        return b - a 
    
    x = b
    while b <= a :
        b +=x
    
    b = b - x 
    return a - b

s , t, n = map(int , input().split())
d = list(map(int , input().split()))
temps = list(map (int , input().split()))
intervalle = list(map(int , input().split()))

for i in range(n) :
    s += d[i]
    s += attente(s , intervalle[i])
    s +=temps[i]

    if s >= t :
        break

print("yes" if s + d[-1] <= t  else "no")