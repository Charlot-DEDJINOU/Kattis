n = int(input())
tA, dA = map(int , input().split())
tB, dB = map(int, input().split())
alice = (tA + (n -1) * dA + tA) * n // 2
bob = (tB + (n -1) * dB + tB) * n // 2

print("Alice" if alice < bob else "=" if bob == alice else "Bob")