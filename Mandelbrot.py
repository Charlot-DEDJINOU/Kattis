def solution(c,r) :
    z=0
    for i in range(r) :
        z = z**2 + c
        if abs(z) > 2:
            return "OUT"
    return "IN"

i=1
while True :
    try :
        x,y,r=map(float,input().split())
        r=int(r)
        print("Case "+str(i)+":",solution(complex(x,y),r))
        i+=1
    except :
        break