number = int(input("Enter a number to countdown from: "))
while number > 0:
    if number>5:
        print(number)
    elif number == 5:
        print('five')
    elif number == 4:
        print('four')
    elif number == 3:
        print('three')                
    elif number == 2:
        print('two')
    elif number == 1:
        print('one')   
    number-=1     