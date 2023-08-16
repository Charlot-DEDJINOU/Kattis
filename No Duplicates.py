s = input().split()
s = "yes" if len([x for x in s if s.count(x) > 1]) == 0 else "no"
print(s)