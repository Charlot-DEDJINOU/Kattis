def main():
    n = int(input())
    tab = [input() for _ in range(n) ]
    s = 0

    for i in range(1, n):
        if tab[i] == tab[i - 1]:
            s += 1

    print(s)

if __name__ == "__main__":
    main()