import os, re, openpyxl, xlsxwriter

cwd = os.getcwd()

for root, dirs, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('_source.json'):
            base = file_path.split("_source.json")[0]
            f = open(file_path, encoding='utf-8', mode='r+')
            ALL_source = re.findall(r'\"text\"\:\"(.*?)\"', f.read())
            ALL_source.insert(0, "source")
            f.close()
            f1 = open(base+'_target.json', encoding='utf-8', mode='r+')
            ALL_target = re.findall(r"\"target_lang_text\"\:\"(.*?[^\\])\"|\"reason\"\:\"(.*?[^\\])\"", f1.read())
            target_column = ['target']

            for i in ALL_target:
                if i[0] != "":
                    target_column.append(i[0])
                else:
                    target_column.append("Secret because: "+i[1])

            dictionary = dict(zip(ALL_source, target_column))

            wb = xlsxwriter.Workbook(base+".xlsx")
            worksheet = wb.add_worksheet()
            n = 2

            row = 0
            col = 0
            for key, value in dictionary.items():
                worksheet.write_string(row, col, key)
                worksheet.write_string(row, col+1, value)
                row+=1

            wb.close()
