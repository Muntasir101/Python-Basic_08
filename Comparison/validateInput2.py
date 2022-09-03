while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print("Password can only have letters and numbers.")
