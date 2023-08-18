from decimal import Decimal

a, b, c = map(Decimal, input().split())
result = a * b / c

decimal_places = 12
formatted_result = "{:.{}f}".format(result, decimal_places)
print(formatted_result)