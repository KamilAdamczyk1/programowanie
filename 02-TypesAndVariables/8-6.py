distance = float(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price / l: '))
fuel_consumption = float(input('Enter fuel consupmtion in l/100km'))

total_fuel_consumption = distance * fuel_consumption
total_cost = total_fuel_consumption * fuel_price

print(f'Total fuel consumption: {total_fuel_consumption}, total cost: {total_cost}')