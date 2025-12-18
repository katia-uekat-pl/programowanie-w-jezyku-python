#First approach:

def first_two_numbers_bigger_than_third (number1: int, number2: int, number3: int) -> bool:
    return number1 + number2 >= number3

the_outcome = first_two_numbers_bigger_than_third(5,5,5)
print(the_outcome)

#Second approach with the list:

def first_two_numbers_bigger_than_third (number1: int, number2: int, number3: int) -> bool:
    return number1 + number2 >= number3

the_numbers = [5,5,5]

the_outcome = first_two_numbers_bigger_than_third(*the_numbers)
print(the_outcome)

#for the logging purpose:
a,b,c = the_numbers

if  the_outcome:
    print(f"The sum of the [{a}] and [{b}] is: [{a+b}], which is bigger or equal to [{c}].")
else:
    print(f"The sum of [{a}] and [{b}] is p{a+b}], which is less than [{c}].")