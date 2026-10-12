first = input('first letter: ')
second = input('second letter: ')
first_code = ord(first)
second_code = ord(second)
how_many = second_code - first_code - 1

if first == second:
    how_many = 0

print(f'Between {first} and {second} is {how_many} letters')
