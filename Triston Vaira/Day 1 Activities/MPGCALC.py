odo1 = input('Enter an odometer reading: ')
odo2 = input('Enter an odometer reading: ')
consumption = input('Enter consumption: ')

# odo2 - odo1 / consumption

mpg = abs(float(odo2) - float(odo1)) / float(consumption)

print('{:.2f}'.format(mpg))
