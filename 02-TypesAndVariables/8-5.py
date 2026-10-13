swift = input('enter your SWIFT code: ')
bank = swift[0:4]
country = swift[4:6]
location = swift[6:8]
branch = swift[8:11]

print(f'Bank code: {bank}')
print(f'Country code: {country}')
print(f'Location code: {location}') 
print(f'Branch code: {branch}')

