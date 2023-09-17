from math import cos , sin , pi
res=[]
tour=int(input())
for i in range(tour) :
    v,angle,x,h1,h2=map(float,input().split(" "))
    angle=pi*angle/180
    h=-0.5*9.81*x*x/(v*v*cos(angle)*cos(angle)) + x*sin(angle)/cos(angle)
    if h <= h1+1 or h >= h2-1 :
        res.append("Not Safe")
    else :
        res.append("Safe")

for r in res :
    print(r)