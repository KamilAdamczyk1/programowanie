amount = int(input('Enter amount: '))

if amount > 0:
    five_rest = amount % 5
    five = amount // 5
    two_rest = five_rest % 2
    two = five_rest // 2
    print(f'Amount of PLN: {amount}')
    print(f'5 PLN coins: {five}')
    print(f'2 PLN coins: {two}')
    print(f'1 PLN coins: {two_rest}')
else:
    print('No coins')