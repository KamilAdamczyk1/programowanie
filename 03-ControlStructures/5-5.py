###
# Sums numbers entered by user
#
total_sum = 0
how_many=''
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    how_many +='|'
    arithmetic_mean = total_sum / len(how_many)
print(f"The total sum of the numbers is: {total_sum}, arithmetic mean is: {arithmetic_mean}")
