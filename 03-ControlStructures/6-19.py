interested = input('Are you interested in computer science? (y/n): ')
playing = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')

if interested == 'y':
    ifinterested = 'Yes'
elif interested == 'n':
    ifinterested = 'No'

if playing == 'y':
    ifplaying = 'Yes'
elif playing == 'n':
    ifplaying = 'No'

if instagram == 'y':
    ifinstagram = 'Yes'
elif instagram == 'n':
    ifinstagram = 'No'

print('Interested in computer science?: ', ifinterested)
print('Do you like playing computer games?: ', ifplaying)
print('Has an Instagram?: ', ifinstagram)