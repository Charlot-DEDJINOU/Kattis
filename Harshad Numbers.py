def moi(n):
    b = 0
    i = 1
    while n // i != 0:
        b += n % (i * 10) // i
        i *= 10
    return b

def main():
    s = int(input())
    i = s

    while i > 0:
        if i % moi(i) == 0:
            print(i)
            break
        i += 1

if __name__ == "__main__":
    main()