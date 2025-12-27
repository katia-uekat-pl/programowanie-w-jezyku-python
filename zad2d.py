def print_every_other_number(list_of_numbers):

    every_other = [list_of_numbers[::2]]
    print("Every other number: ", every_other)


the_list = list(range(10))


print_every_other_number(the_list)
