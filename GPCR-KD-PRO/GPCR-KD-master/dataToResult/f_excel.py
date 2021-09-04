import openpyxl
import re

wb = openpyxl.load_workbook('result.xlsx')


sheet = wb.worksheets[0]

list_of_record = []
with open("result_r","r") as f:
    for row in f.readlines():
        sequ = row.strip("\n")
        t = re.split(r" +",sequ)
        list_of_record.append(t)


for i in range(1,7):
    for j in range(1,8):
        sheet.cell(i,j).value = list_of_record[i-1][j-1]


wb.save("result.xlsx")