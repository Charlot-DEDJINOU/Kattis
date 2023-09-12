for i in range(1 , int(input()) + 1) :
    g = int(input())
    g = list(map(int , input().split()))
    for x in g :
        if g.count(x) == 1 :
            print("Case #",i,": ",x,sep="")
            break