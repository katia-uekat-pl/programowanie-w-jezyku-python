the_list = list(range(10))


# "one approach:
def display_even_numbers_1(list_of_numbers):
    for number in list_of_numbers:
        if number % 2 == 0:
            print(number)


display_even_numbers_1(the_list)


# "second approach:
def print_even_numbers_2(list_of_numbers):
    evens = [x for x in list_of_numbers if x % 2 == 0]
    print(evens)


print_even_numbers_2(the_list)
