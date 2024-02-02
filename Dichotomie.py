def dichotomie(tab, item):
    a = 0
    b = len(tab) - 1
    while a <= b:
        m = (a + b) // 2
        if tab[m] == item:
            return True
        elif tab[m] < item:
            a = m + 1
        else:
            b = m - 1
    
    return False


tab = list(map(int , input().split()))
n = int(input())
print(dichotomie(tab,n))