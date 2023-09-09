def main():
    e, r = map(int, input().split())
    tab = list(map(int, input().split()))
    res = []
    
    for _ in range(r):
        t, dp, des = map(int, input().split())
        
        if t == 1:
            tab[dp - 1] = des
        else:
            res.append(abs(tab[des - 1] - tab[dp - 1]))
    
    for val in res:
        print(val)

if __name__ == "__main__":
    main()