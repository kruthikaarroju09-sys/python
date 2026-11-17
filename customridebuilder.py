print('========================================================')
print('                 welcome to ride bulder!!                 ')
print()

print('step 1: pick your vehicle')
print('   1 - bike')
print('   2 - car')
print()

choice = int(input('enter 1 or 2 :   '))

if choice == 1:
    print('step 2: pick your bike type')
    print('1 - scooty')
    print ('2 - mountain bike')
    print()

    bike_type = int(input('enter 1 or 2: '))

    if bike_type == 1:
        print('you picked  : scooty')
        print('top speed  : 80 km/h')
        print('best for  :city roads')
    else:
        print('you picked  : mountain bike')
        print('top speed  : 40 km/h')
        print('best for  :off-road traills')

elif choice == 2:
    print('step 2: pick your car type')
    print('1 - sedan')
    print ('2 - SUV')
    print()

    car_type = int(input('enter 1 or 2: '))

    if car_type == 1:
        print('you picked  : sedan')
        print('seat  : 5 passengers')
        print('best for  :family trip')
    else:
        print('you picked  :suv')
        print('seat  :  7 passengers')
        print('best for  :off-road adventures')

