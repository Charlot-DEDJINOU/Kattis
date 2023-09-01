from math import sin , pi , floor

h , v = map(int , input().split())
v = h/sin(pi*v/180)

print(v if floor(v) == v else floor(v) + 1)