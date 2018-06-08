num = int(input('Enter the Number: '))
exp = int(input('Enter the Exponent: '))
result = 1
for i in range(1,(exp+1)):
    result = result * num
print('The result is: ',result)
