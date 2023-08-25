first = input()
second = input()
first = [1 for i in range(4) if first[i] != second[i]]
print(pow(2 , sum(first)))