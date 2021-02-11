import pywhatkit
from datetime import date
today = date.today()
import time
import xlrd
from datetime import date

today = date.today()
t=time.localtime()
loc = ("birthdaylist.xlsx")


wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

curdate=(str(today.day)+"-"+str(today.month))
for i in range(sheet.nrows):
    if curdate==sheet.cell_value(i, 1):
    	number=(sheet.cell_value(i,0))
    	message=(sheet.cell_value(i,2))
    	pywhatkit.sendwhatmsg(number,message,int(time.strftime("%H",t)),int(time.strftime("%M",t))+2)

