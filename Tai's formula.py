def trapezeAir(a , b) :
    return (a[1] + b[1])*(b[0] - a[0])/2

aire = 0
a , b = 0 , 0
for i in range(int(input())) :
    if i == 0 :
        a = list(map(float , input().split()))
    else :
        b = list(map(float , input().split()))
        aire += trapezeAir(a , b)
        a = b

print(round(aire/1000 , 6))