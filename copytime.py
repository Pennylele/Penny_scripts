import os, re

response = input("what target file do you want to copy the source timing to? ")
source = open("source.srt", encoding="utf-8", mode="r+")
target = open(response, encoding="utf-8", mode="r+")

sourceCodes = re.findall(r"\d+\n\d\d:\d\d:\d+,\d+\s-->\s\d\d:\d\d:\d+,\d+\n", source.read())
subNo = len(sourceCodes)
targetText = re.findall(r":\d+,\d+\n(.*?)\n\n", target.read(), re.DOTALL)
source.close()
target.close()

target = open(response, encoding="utf-8", mode="r+")
lastLine = re.findall(str(subNo) + r"\n\d\d:\d\d:\d+,\d+\s-->\s\d\d:\d\d:\d+,\d+\n(.*)", target.read(), re.DOTALL)
for i in lastLine:
    targetText.append(i)
print(targetText)

combination = dict(zip(sourceCodes, targetText))
f = open(os.path.splitext(response)[0]+"_new.srt", encoding="utf-8", mode="w+")
for key, value in combination.items():
    f.write(key+value+"\n\n")