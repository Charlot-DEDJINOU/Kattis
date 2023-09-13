def main():
    n = int(input())
    for _ in range(n):
        a, b, c = map(float, input().split())
        if a + b == c or abs(a - b) == c or a * b == c or a / b == c or b / a == c:
            print("Possible")
        else:
            print("Impossible")

if __name__ == "__main__":
    main()