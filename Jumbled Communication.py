def decrypt(b):
    r = 0

    mask = 1
    for i in range(8):
        next_bit = (b ^ r) & mask
        r |= next_bit << 1
        mask = mask << 1

    return r >> 1


n = int(input())
numbers = list(map(int, input().split()))
print(*[decrypt(x) for x in numbers])
