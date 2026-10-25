car_speed = int(input('Enter car speed in km/h: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed >=speed_limit_min and car_speed<=speed_limit_max:
    print('Valid car speed')
else:
    print('Invalid car speed')