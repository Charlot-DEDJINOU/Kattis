def main():
    a = 0
    b = 1
    n = int(input())
    
    if n == 1:
        print(a, b)
    else:
        for _ in range(n - 1):
            temp = a + b
            a = b
            b = temp
        print(a, b)

if __name__ == "__main__":
    main()
