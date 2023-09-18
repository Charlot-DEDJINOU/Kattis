from math import pi

alphabet = [chr(ord('A') + i) for i in range(26)] + [' ' , "'"]
p = 60 * pi
t = p/28 / 15

for _ in range(int(input())) :
    s = input()
    depart = alphabet.index(s[0])
    temps = 1
    for x in s[1:] :
        index = alphabet.index(x)
        distance = min(abs(depart - index) ,  28 - abs(depart - index))
        temps += 1 + distance*t
        depart = index

    print(temps)

