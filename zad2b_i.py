def multiply_by_two(numbers):
    result_list = []
    for number in numbers:
        result_list.append(number * 2)
    return result_list


the_list = [1, 2, 3, 4, 5]
for_logging = multiply_by_two(the_list)
print(for_logging)
