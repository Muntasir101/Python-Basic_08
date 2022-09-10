birthdays = {'Alice': 'Apr 1', 'Bob': 'May 1', 'batman': 'mar 1'}

while True:
    print("Enter your name: ")
    name = input()
    if name == '':
        print("Please enter your name")

    else:
        if name in birthdays:
            print(birthdays[name] + " Is Your birthday.")
            break

        else:
            print("You dont have birthday")
