import pyinputplus as pyinput

email = pyinput.inputEmail(prompt='Enter your Email: ')
print("Thanks for your Email Address")

password = pyinput.inputStr(prompt='Enter your password: ')
print("Thanks for using your password")

age = pyinput.inputNum(prompt='Enter your Age: ', min=0, max=100, blank=True)
print("Thanks for your valid age")

name = pyinput.inputStr(prompt='Enter your Name: ')
print("Thanks for your Name")

print(f'My information {name},{email},{password},{age}')
