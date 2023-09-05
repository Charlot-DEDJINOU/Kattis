def main():
    x = int(input())
    n = int(input())
    b = x
    for i in range(n):
        a = int(input())
        if a > x:
            x = 0
        else:
            x -= a
        x += b
    print(x)

if __name__ == "__main__":
    main()