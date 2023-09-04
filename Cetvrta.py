def main():
    tab = []
    for _ in range(3):
        x, y = map(int, input().split())
        tab.append((x, y))

    a = b = 0

    for i in range(3):
        if tab[(i + 1) % 3][0] == tab[(i + 2) % 3][0]:
            a = tab[i][0]
        if tab[(i + 1) % 3][1] == tab[(i + 2) % 3][1]:
            b = tab[i][1]

    print(a, b)

if __name__ == "__main__":
    main()