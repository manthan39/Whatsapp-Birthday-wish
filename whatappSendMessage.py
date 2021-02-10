# Reading an excel file using Python
import xlrd
from datetime import date
today = date.today()


# Give the location of the file
loc = ("C:\\Users\\mvbhatiya\\Desktop\\birthdaylist.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
# print(sheet.cell_value(0, 0))
# print(sheet.nrows)
curdate=(str(today.day)+"-"+str(today.month))
for i in range(sheet.nrows):
    if curdate==sheet.cell_value(i, 1):
    	name=(sheet.cell_value(i,0))
    	message=(sheet.cell_value(i,2))


print(name)
print(message)
    	


