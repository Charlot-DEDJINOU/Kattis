cor = {
    0 : [0,0] ,
    2 : [0,1] ,
    1 : [1,0] ,
    3 : [1,1]
}

n = input()
x = [0 , 0]

for i in range(0,len(n)) :
    y = cor[int(n[i])].copy()
    y[0] *= 2**(len(n) -1 - i)
    y[1] *= 2**(len(n) -1 - i)

    x[0] += y[0]
    x[1] += y[1]

print(len(n) , *x)