num = int(input('Enter the number: '))
for i in range(1,num+1):
    print('\t')
    for j in range(1,11):
        print(i,'X',j,'=',i*j)
