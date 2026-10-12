import random
computers = random.randint(1,6)
users = int(input("guess computers roll: "))
won = computers == users

print(f'computer rolled {computers}')
print(f'you guessed {users}')
print(f'You won: {won}')