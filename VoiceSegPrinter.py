import os, openpyxl, shutil

num = {}
for i, j, y in os.walk('.'):
    for each in j:
        os.chdir(each) 
        try:
            os.remove('.DS_Store')
        except:
            pass
        number = len(os.listdir())
        name = os.path.basename(each)
        num[name] = number
        os.chdir("..")


for file in os.listdir(os.getcwd()):
    if file.endswith(".xlsx"):
        filename = os.path.splitext(file)[0]
        segNum = filename.split("_")[0]
        number = num[str(segNum)]
        links = []
        for i in range(1, number+1):
            if i < 10:
                links.append("=HYPERLINK(\"Marker 0" + str(i) + ".mp3\")")
            else:
                links.append("=HYPERLINK(\"Marker " + str(i) + ".mp3\")")

        wb = openpyxl.load_workbook(file)
        worksheet = wb.active

        worksheet.cell(row=1, column=12).value = "Audio Files"
        r = 2
        for n in links:
            if worksheet.cell(row=r, column=12).fill.bgColor.value != '00000000':
                r+=1
                worksheet.cell(row=r, column=12).value = n
                r+=1
                continue
            else:
                worksheet.cell(row=r, column=12).value = n
                r+=1

        os.chdir(segNum)
        wb.save(file + '_forQA.xlsx')
        os.chdir("..")
        os.system("zip -r " + segNum + ".zip " + segNum)

