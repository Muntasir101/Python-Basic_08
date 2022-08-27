print('Enter Marks')
marks = int(input())

if marks>=0 and marks<=33:
    print("Grade F")

elif marks>=34 and marks<=39:
    print("Grade D")

elif marks>=40 and marks<=49:
    print("Grade C")

elif marks>=50 and marks<=59:
    print("Grade B")

elif marks>=60 and marks<=69:
    print("Grade A-")

elif marks>=70 and marks<=79:
    print("Grade A")

elif marks>=80 and marks<=100:
    print("Grade A+")

else:
    print("Invalid Marks")