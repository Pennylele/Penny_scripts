import csv, os

path = os.getcwd()
for files in os.listdir(path):
    if files.endswith('.csv'):
        with open(files, newline='', encoding='utf-8') as csvfile:
            foldername = files.split(".")[0]
            os.mkdir(foldername)
            os.chdir(foldername)
            reader = csv.DictReader(csvfile)
            n = 1
            for row in reader:
                f_source = open(str(n)+"_source.json", 'w+', encoding='utf-8')
                f_source.write(row['column.name1'])
                f_source.close()
                f_target = open(str(n)+"_target.json", 'w+', encoding='utf-8')
                f_target.write(row['column.name2'])
                f_target.close()
                n += 1
        os.chdir("..")

ALL_source = []
for root, dirs, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.json') and os.path.getsize(file_path) == 0:
            source_filename = file_path.split("_target.json")[0]+"_source.json"
            ALL_source.append(source_filename)
            os.remove(file_path)

       
for i in ALL_source:
    os.remove(i)    