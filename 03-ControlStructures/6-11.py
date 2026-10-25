Current = float(input('Enter current price: '))
Previous = float(input('Enter previous price: '))
discount = (Previous-Current)/Previous*100
print(f'Current price: {Current}')
print(f'Previous price: {Previous}')
if discount > 10:
    print('Buy the product')
else:
    print('Dont buy the product')
print(f'Product reduced by {discount}%')