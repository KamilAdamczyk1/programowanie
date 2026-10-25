pin_set = '1234'
pin=input('Enter pin: ')
if pin==pin_set:
    print('You are in')
else:
    print("Incorrect")
    pin2=input('Enter pin: ')
    if pin2==pin_set:
        print('You are in')
    else:
        print('Incorrect')
        pin3=input('Enter pin: ')
        if pin3==pin_set:
            print('You are in')
        else:
            print('Incorrect')
            print('Sorry, your payment card has been blocked')