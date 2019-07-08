import os, re, io
import codecs

cwd = os.getcwd()

for file in os.listdir(cwd):
    full = open("all.srt",encoding='utf-8', mode='a+')
    if file.endswith(".srt"):
        f = open(file, encoding='utf-8', mode="r+")
        for line in f.readlines():
            #print(line)
            full.write(line)

    f = open("all.txt", encoding='utf-8', mode='w')
    text = re.sub(r"1\n", "\n"+"1", f.read())
    f2.write(text)
    f2.close()


