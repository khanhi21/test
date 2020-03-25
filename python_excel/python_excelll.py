# Lets create an excel file using python

import xlsxwriter

data9 = xlsxwriter.Workbook("data9.xlsx")
# creating a workbook using the builtin method and assigning a name to our file.

worksheet = data9.add_worksheet("data9.xls")

# note - rows and columns are zero indexed
# The first cell in a worksheet A1 is (0, 0), B1 is (0, 1)

worksheet.write("A1", "Everyone")
worksheet.write("B1", "Khanhi")
worksheet.write("C1", "Vivek")
worksheet.write("D1", "Yin")
worksheet.write("E1", "Weiyee")
worksheet.write("F1", "Andy")
worksheet.write("G1", "Gigi")
worksheet.write("H1", "Ben")
worksheet.write("I1", "CJ")
worksheet.write("J1", "Sassy")
worksheet.write("K1", "Jonny")
worksheet.write("L1", "Shugs")
worksheet.write("M1", "Vijay")
worksheet.write("N1", "Tossin")
# data9.cell(row = 1, column = 1).value = "changed"
# using the bullirin write method we inserted data to our file

data9.close()
# print(row)
# print(column)
# print(content)
# print(workbook)
print(data9)