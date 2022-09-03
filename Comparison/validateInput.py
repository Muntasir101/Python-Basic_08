while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Invalid.Please Enter your age as Number only")

