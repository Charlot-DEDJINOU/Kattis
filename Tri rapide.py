def sort(array):

    left = []
    equal = []
    right = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                right.append(x)

        return (
            sort(left) + equal + sort(right)
        )  
    
    else:
        return array

tab = list(map(int , input().split()))
print(sort(tab))