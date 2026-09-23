numbers = [1 ,2, 3, 4, 5, 6, 7, 8]

if len(numbers) == 0:
    result = [[], []]

elif len(numbers) % 2 == 0:
    middle = (len(numbers) + 1) // 2
    result = [numbers[:middle], numbers[middle:]]
else:
    middle = len(numbers) // 2 + 1
    result = [numbers[:middle], numbers[middle:]]

print(result)