print('=== start school day planner ===')
print('answer 3 quick question and I will plan your day!\n')

day = input('what day is it? monday to sunday : ').strip().lower()
weather = input('what is the weather? sunny / rainy / clodudy : ').strip().lower()
homework = input('is your homework done? yes / no : ').strip().lower()
print()
print(f'='*35)

if day in ('saturday', 'sunday'):
    print('day type  : weekend - enjoy your free time!')
elif day == 'monday':
    print('day type   : first day of the week. pack your weekly planner.')
elif day == 'friday':
    print('day type   : last schoolday. return library books today.')
elif day in('tuesday', 'wednesday', 'thursday'):
    print('day typr   : regurlar school day. stay focused!')
else:
    print('day not recongnised cheek your spelling')