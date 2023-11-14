h , l , n = map(int , input().split())
briques = list(reversed(list(map(int , input().split()))))
i , som = 0 , 0

while briques :
    som += briques.pop()
    if i == h :
        break

    if som > l :
        break
    elif som == l :
        i += 1
        som = 0

print("YES" if i == h else "NO")