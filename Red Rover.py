def minimize_instructions(route):
    n = len(route)
    result = n  

    for end in range(1, n + 1):
        for start in range(end):
            macro = route[start:end]
            if len(macro) < len(route)//2+1 :
                macro_expansion = route.replace(macro, 'M')

                new_length = len(macro_expansion) + len(macro)

                result = min(result, new_length)

    return result

route = input().strip()

min_length = minimize_instructions(route)
print(min_length)
