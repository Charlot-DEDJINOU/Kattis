def rejected_groups(n, m, groups):
    seats = n
    rejected = 0
    for group in groups:
        if seats >= group:
            seats -= group
        else:
            rejected += 1
    return rejected

n, m = map(int, input().split())
groups = list(map(int, input().split()))
print(rejected_groups(n, m, groups))