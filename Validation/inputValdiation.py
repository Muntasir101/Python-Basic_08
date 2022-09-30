while True:

    print("Enter your age: ")
    age = input()

    try:
        age = int(age)

    except:
        print("Please enter your age in numeric")
        continue

    if age < 0:
        print("Please enter your age in positive")
        continue

    break

print(f'Your Age is {age}')
