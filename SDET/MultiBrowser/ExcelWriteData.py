'''
Created on 07-Aug-2019

@author: Amitava
'''
import openpyxl

path="E:\PythonExcelDataWrite.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active    

# workbook.get_sheet_by_name(sheet)

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="Amitava"
workbook.save(path)