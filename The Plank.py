n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for planche in [1, 2, 3]:
        if i >= planche:
            dp[i] += dp[i - planche]

print(dp[n])