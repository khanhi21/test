
import xlsxwriter

data9 = xlsxwriter.Workbook("data9.xlsx")
worksheet = data9.add_worksheet("Data_9.xlsx")
worksheet.write("A1", "Data 9")
worksheet.name = "Data 9 Team"
data9.close