print('enter a number (numertor):   ')
numn = int(input())
print('enter a number (denominator):  ')
numd = int (input())

if numn%numd==0:
    print('is divisible by' +str(numd))
else:
    print('is not divisible by' +str(numd))