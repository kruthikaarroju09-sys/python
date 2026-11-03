temperature = int(input("enter today's temperature in celsius"))
if temperature < 20:
    outfit = 'jacjet'
    print('it is cold today.')
    print('were a', outfit)
else:
    outfit = 't-shirt'
    print('it is a warm today.')
    print ('were a', outfit)

is_raining = input('is it raining today (yes/no):')
if is_raining == 'yes':
    print('bring an umbrella!')

wind_speed = int(input('enter the wind_speed in kilometter per hour'))
if wind_speed > 30:
    needs_windbreaker = 'yes' 
    print('it is windy today.')
else:
    needs_windbreaker = 'no'
    print('it is calam today')
    print('no windbreaker needed over your',outfit)
