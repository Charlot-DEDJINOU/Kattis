g , d = map(int , input().split())
if g == d == 0 : print("Not a moose")
elif g == d : print("Even",g*2)
else : print("Odd",max(g,d)*2)