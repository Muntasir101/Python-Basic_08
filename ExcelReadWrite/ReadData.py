import Common_Functions

file = "TestData.xlsx"
sheet = "Sheet1"

number_of_rows = Common_Functions.get_row_count(file, sheet)
print(number_of_rows)

number_of_columns = Common_Functions.get_column_count(file, sheet)
print(number_of_columns)

# All Row Data
for i in range(2, number_of_rows + 1):
    row_data = Common_Functions.read_data(file, sheet, i, 1)
    print(row_data)

# All Column Data in 2nd Column
for i in range(2, number_of_rows + 1):
    column_data = Common_Functions.read_data(file, sheet, i, 2)
    print(column_data)

# All Column Data in 3nd Column
for i in range(2, number_of_rows + 1):
    column_data = Common_Functions.read_data(file, sheet, i, 3)
    print(column_data)