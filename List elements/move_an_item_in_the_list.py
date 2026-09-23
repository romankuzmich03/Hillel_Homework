numbers = [12, 3, 4, 10, 125, 1, 23, 4]

if len(numbers) > 1:
    last_element = numbers.pop()
    numbers.insert(0, last_element)

print(numbers)