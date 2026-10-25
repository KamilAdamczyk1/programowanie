time=input('Enter time in 24h format: ')
hour=int(time[0:2])
min=int(time[3:5])
if hour > 12 and hour < 24:
    hour -= 12
    print(f'Time in 12h format: {hour}:{min}')
elif hour > 24 and min > 60:
    print('Wrong')
else:
    print('time in 12h format', hour,':',min)