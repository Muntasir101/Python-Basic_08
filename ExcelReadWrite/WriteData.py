import Common_Functions

file = "TestData.xlsx"
sheet = "Sheet1"

number_of_rows = Common_Functions.get_row_count(file, sheet)
print(number_of_rows)

number_of_columns = Common_Functions.get_column_count(file, sheet)
print(number_of_columns)

for i in range(2, number_of_rows + 1):
    Common_Functions.write_data(file, sheet, i, 4, "Test")
