def list_operations(list1: list, list2: list) -> list:

    unique_elements = set(list1 + list2)
    return [x**3 for x in unique_elements]


print(list_operations([1, 1, 4], [1, 9, 1]))


# "Alternative approach with for each:
def list_operations(list1: list, list2: list) -> List:
    unique_elements = set(list1 + list2)
    outcome_list = []

    for element in unique_elements:
        given_power = element ** 3
        outcome_list.append(given_power)

    return outcome_list


print(list_operations([1, 1, 4], [1, 9, 1]))
