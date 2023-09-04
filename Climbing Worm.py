def main():
    a, b, c = map(int, input().split())
    v = a
    i = 0
    while a < c:
        a = a - b + v
        i += 1
    print(i + 1)

if __name__ == "__main__":
    main()