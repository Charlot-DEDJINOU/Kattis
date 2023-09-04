def main():
    n = int(input())
    i, l, cmp = 1, 1, 0

    while l <= n:
        i += 2
        l = l + i * i
        cmp += 1

    print(cmp)

if __name__ == "__main__":
    main()