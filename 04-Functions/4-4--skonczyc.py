any_number = int(input('Enter integer number'))

def sum_digits(any_number):
    abs_number = abs(any_number)
    str_number = str(abs_number)
    for i in len(str_number):
        sum_up = 0
        sum_up += int(str_number[i])
    return sum_up

print(f'The sum of the digits in the number {any_number} is {sum_digits(any_number)}')