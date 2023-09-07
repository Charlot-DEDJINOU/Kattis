def main():
    p, n = float(input()) , int(input())
    c = 0.0
    
    for _ in range(n):
        a, b = map(float, input().split())
        c += a * b
    
    result = c * p
    print(result)

if __name__ == "__main__":
    main()