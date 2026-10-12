car_number = input('Enter car registration number: ')
car_number = car_number.upper()
print(f'Car is from Krakow: {car_number[0:2] == "KR" or car_number[0:2] == "KK"}')