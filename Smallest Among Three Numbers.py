num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
num3 = int(input('Enter Third Number: '))

if (num1 <= num2) and (num1 <= num3) :
    snum = num1
elif (num2 <= num1) and (num2 <= num3) :
    snum = num2
else:
    sum = num3

print('The Smallest number among', num1, ',', num2, 'and', num3, 'is', snum)