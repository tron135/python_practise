num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3rd Number: '))

if((num1>num2) & (num1>num3)):
    print(num1,'is the greatest number.')
elif((num2>num1) & (num2>num3)):
    print(num2,'is the greatest number.')
else:
    print(num3,'is the greatest number.')
