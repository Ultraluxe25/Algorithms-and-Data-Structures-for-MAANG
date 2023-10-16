numbers = [-1, -3, 2, 4, 5, 7, 8, 9]
n = len(numbers)

search_value = 9
left, right = 0, n - 1

while left <= right:
    middle = (left + right) // 2
    value = numbers[middle]

    if value == search_value:
        print(f'{value} with index {middle}')
        break
    elif value < search_value:
        left = middle + 1
    elif value > search_value:
        right = middle - 1
else:
    print('Value hasn\'t been found')
