import os, openpyxl

for file in os.listdir('.'):
    if file.endswith('xlsx'):
        wb = openpyxl.load_workbook(file)
        worksheet = wb.active
        row_count = worksheet.max_row

        for i in range(1, row_count+1):
            f = open(str(i)+".txt", mode="w")
            f.write(worksheet.cell(row=i, column=1).value+"\n")

        os.makedirs(os.path.splitext(file)[0] + "TXT")

        for TXT in os.listdir('.'):
            if TXT.endswith('.txt'):
                os.rename(TXT, str(os.path.splitext(file)[0])+"TXT/"+TXT)



