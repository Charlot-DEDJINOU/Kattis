def moi(n):
    s = 0
    i = 1
    while n // i != 0:
        s += n % (i * 10) // i
        i *= 10
    return s

def main():
    tab = []
    l = -1
    while True:
        l += 1
        a = int(input())
        if a == 0:
            break
        i = 11
        while moi(a) != moi(i * a):
            i += 1
        tab.append(i)
    
    for i in range(l):
        print(tab[i])

if __name__ == "__main__":
    main()