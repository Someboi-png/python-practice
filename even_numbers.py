def even_numbers(numbers):
    results = []

    for number in numbers:
        if number % 2 == 0:
            results.append(number)

    return results

first_list = [3, 4, 7, 10, 2]
second_list = [1, 6, 9, 8]

print(f"Четные из первого списка: {even_numbers(first_list)}")
print(f"Четные из второго списка: {even_numbers(second_list)}")