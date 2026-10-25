set_PIN = '1234'
correct = False
while correct != True:
    PIN = input("Enter PIN: ")
    if PIN == set_PIN:
        print("You're in")
        correct=True
        break
    else:      
        print('Wrong PIN')
        change = input('Would you like to change PIN? (Y/N)')
        if change == 'N':
            if PIN==set_PIN:
                print("You're in")
                correct=True
                break 
            else:
                print('Try again')
        elif change == 'Y':
            changed_PIN = input('Enter new PIN')
            if changed_PIN.isdigit() and len(changed_PIN)==4:
                changed_PIN=set_PIN  
                continue 
            else:
                print('PIN must be 4 digits')
        continue
            



            # nie było podanego kodu w prezentacji, sam spróbowałem