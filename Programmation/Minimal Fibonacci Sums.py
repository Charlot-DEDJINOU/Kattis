def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_sum(n, fib_seq):
    result = []
    for i in range(len(fib_seq) - 1, -1, -1):
        if n >= fib_seq[i]:
            result.append(fib_seq[i])
            n -= fib_seq[i]
    return result

def shortest_fibonacci_representation(n):
    fib_seq = fibonacci_sequence(n)
    fib_sum = fibonacci_sum(n, fib_seq)
    return ' '.join(map(str, reversed(fib_sum[0:len(fib_sum)-1])))

n = int(input())
print(shortest_fibonacci_representation(n))