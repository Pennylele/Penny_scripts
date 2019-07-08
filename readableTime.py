import os, re
from datetime import datetime
import datetime
import decimal

cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith(".csv"):
        f = open(file, mode="r+")
        startlist = []
        durationlist = []
        ff = open(os.path.splitext(file)[0] + ".gTime", mode="a")
        ff.write("Start (target)" + "\n")
        for line in f.readlines():
            start = str(line).split("\t")[1]
            duration = str(line).split("\t")[2]
            startlist.append(start)
            durationlist.append(duration)

        for s, d in zip(startlist[1:], durationlist[1:]):
            try:
                x = datetime.datetime.strptime(s, '%M:%S.%f')
                c = datetime.timedelta(0, (x.minute * 60 + x.second + x.microsecond / 1000000))
                conversion = re.sub(r"(\.\d\d\d)\d{3}", r"\1", str(c))
                ff.write(conversion+"\n")
            except ValueError:
                x = datetime.datetime.strptime(s, '%H:%M:%S.%f')
                c = datetime.timedelta(0, (x.hour*3600 + x.minute * 60 + x.second + x.microsecond / 1000000))
                conversion = re.sub(r"(\.\d\d\d)\d{3}", r"\1", str(c))
                ff.write(conversion+"\n")

        ff.write("\n" + "End (target)" + "\n")
        for s, d in zip(startlist[1:], durationlist[1:]):
            try:
                x = datetime.datetime.strptime(s, '%M:%S.%f')
                y = datetime.datetime.strptime(d, '%M:%S.%f')
                a = datetime.timedelta(0, (x.minute * 60 + x.second + x.microsecond / 1000000))
                b = datetime.timedelta(0, (y.minute * 60 + y.second + y.microsecond / 1000000))
                z = a + b
                conversion = re.sub(r"(\.\d\d\d)\d{3}", r"\1", str(z))
                #number = decimal.Decimal(str(z))
                #rounded = number.quantize(decimal.Decimal('.01'), rounding='ROUND_HALF_UP')
                #conversion = re.sub(r"(\d{1,})\.00", r"\1", str(rounded))
                #conversion2 = re.sub(r"(\d{1,}\.\d)0", r"\1", conversion)
                #conversion3 = re.sub(r"(\d{1,})\.0$", r"\1", conversion2)
                ff.write(conversion+"\n")
            except ValueError:
                x = datetime.datetime.strptime(s, '%H:%M:%S.%f')
                y = datetime.datetime.strptime(d, '%M:%S.%f')
                a = datetime.timedelta(0, (x.hour*3600 + x.minute * 60 + x.second + x.microsecond / 1000000))
                b = datetime.timedelta(0, (y.minute * 60 + y.second + y.microsecond / 1000000))
                z = a + b
                conversion = re.sub(r"(\.\d\d\d)\d\d\d", r"\1", str(z))
                #number = decimal.Decimal(str(z))
                #rounded = number.quantize(decimal.Decimal('.01'), rounding='ROUND_HALF_UP')
                #conversion = re.sub(r"(\d{1,})\.00", r"\1", str(rounded))
                #conversion2 = re.sub(r"(\d{1,}\.\d)0", r"\1", conversion)
                #conversion3 = re.sub(r"(\d{1,})\.0$", r"\1", conversion2)
                ff.write(conversion+"\n")

