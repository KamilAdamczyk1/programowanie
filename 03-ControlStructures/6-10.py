dog_age = float(input("Enter dog's age in human years: "))
if dog_age > 2:
    in_human = 2*10.5+(dog_age-2)*4
    print(f'The dog"s age in dog"s years is {in_human} years')
elif dog_age<2:
    in_human = 'between 0 and 10.5'
    print(in_human)
