start , end = map(int , input().split())
print(len([1 for x in range(start , end + 1) if len([1 for i in str(x) if i != '0' and str(x).count(i) == 1 and x % int(i) == 0]) == len(str(x))]))