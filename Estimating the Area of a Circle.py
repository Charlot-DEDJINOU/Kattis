from math import pi

while True :
    r,m,c = map(float , input().split())
    if r == 0 and m == 0 and c == 0 :
        break
    else :
        m = c/m
        c = 2*r
        c = c*c*m

        print(r*r*pi , c ,sep=" ")