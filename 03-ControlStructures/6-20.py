decimal = int(input('Enter decimal number: '))
binary=''
while decimal > 0:
    reminder = decimal % 2
    binary = str(reminder) + binary
    decimal = decimal // 2

print(binary)