from math import cos
from math import pi
l , a = map(int , input().split())
if 0 <= a <= 180 :
    print("safe")
elif a == 270 :
    print(l)
else :
    a = 90 - (a - 180) if 180 < a < 270 else 90 - (360 - a)
    a = a*pi/180
    print(abs(int(l/cos(a))))
