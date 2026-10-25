###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 8
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print('It is hot')
elif temperature > 15:
    print('It is warm')
elif temperature>=0:
    print('it is cold')
elif temperature<0:
    print('warning, frost')
