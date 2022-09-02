name = ''
password = ''

while name != 'superman' and password != 'superhero':
    print('Please enter your name: ')
    name = input()
    print("Please enter your password: ")
    password = input()

    if name == 'superman' and password == 'superhero' :
        print("Thank you.Access Granted")
    else:
        print("Access Rejected.Please try again")

    continue

