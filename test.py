import time
import openpyxl
def now():
    time()

def B():
  print("this is gitflow")

def write_excel_template(filename, sheetname, datalist):
    excel_file = openpyxl.Workbook
    excel_sheet = excel_file.active
    excel_sheet.column_dimensions['A'].width =100
