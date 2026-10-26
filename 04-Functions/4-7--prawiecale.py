def time_string(hours, minutes, time_format):
    time =''
    if time_format == '12':
        if hours > 12:
            time = (f'{hours - 12}:{minutes}pm')
        else:
            time = (f'{hours}:{minutes}am')
    elif time_format == '24':
        time = (f'{hours}:{minutes}')
    
    return time
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12') )
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))

