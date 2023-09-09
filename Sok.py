v = list(map(int , input().split()))
p = list(map(int , input().split()))
rapport = [v[i] / p[i] for i in range(3)]
m = rapport.index(min(rapport))
rt = rapport[m]

print(*[round(v[i] - p[i]*rt , 7) for i in range(3)])
