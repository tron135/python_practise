num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))

try:
    num3 = num1/num2

except:
    print('You can\'t divide the number by zero')

else:
    print(num3)
