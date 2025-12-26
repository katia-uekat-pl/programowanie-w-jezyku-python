def if_even_number(number: int) -> bool:
    return number % 2 == 0


the_number = 1000
the_outcome = if_even_number(the_number)

if the_outcome:
    print("Even number")
else:
    print("Odd numer")
