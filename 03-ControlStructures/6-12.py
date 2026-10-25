number = int(input('Enter number of products purchased: '))
price = float(input('Enter number price of product: '))

if number > 2:
    total = 2*price+(number-2)*0.75*price
    print('Amount to pay: ', total)