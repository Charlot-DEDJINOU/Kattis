n , w , l = map(int , input().split())
h = ((w**2) + (l**2))**0.5
for _ in range(n) :
    if int(input()) <= h :
        print("DA")
    else :
        print("NE")