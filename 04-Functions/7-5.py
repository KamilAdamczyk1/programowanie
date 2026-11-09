import betweenrange

number = int(input('Enter a number: '))
x = int(input('Enter a min number: '))
y = int(input('Enter a max number: '))

returned = betweenrange.between(number, x, y)

print(f'Number {number} in the range <{x},{y}>: {returned}')