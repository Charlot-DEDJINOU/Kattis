n , p , s = map(int , input().split())
for _ in range(s) :
    if p in list(map(int , input().split()[1:])) :
        print("KEEP")
    else :
        print("REMOVE")