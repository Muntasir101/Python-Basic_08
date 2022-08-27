student1 = ['devid', 'mail@gmail.com', '12345678', 'dhaka']

# Simple dictionary
car = {
    'make': 'bmw',
    'model': 'bw22',
    'year': 2022
}

# Nested dictionary
user = {
    'name': 'smith',
    'age': 30,
    'location':
        {
            'present_address': {
                'road': '01',
                'house': '002',
            },
            'permanent_address': 'CTG'
        }
}

print(car['year'])
print(user['location']['present_address']['road'])
print(car.values())

favorite_color = {
    'smith': 'red',
    'kevin': 'blue',
    'david': 'green'
}

# smith's favorite color is red
# kevin's favorite color is blue
# david's favorite color is green

for name in favorite_color.keys():
    print(name.title())

for color in favorite_color.values():
    print(color.title())

for name, color in favorite_color.items():
    print(f"{name.title()}'s favorite color is {color.title()}.")
