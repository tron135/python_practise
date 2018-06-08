password = 'williams'
for i in range(3):
    pwd = input('Enter the Password: ')
    j = 2
    if(pwd == password):
        print('Welcome!!!')
        break
    else:
        print('Wrong Password and chances left',j-i)

