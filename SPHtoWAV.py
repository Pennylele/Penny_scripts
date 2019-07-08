import os, re, io, shutil
import codecs

cwd = os.getcwd()
os.makedirs("WAVs")

for file in os.listdir(cwd):
    if file.endswith(".sph"):
        os.system("sph2pipe.exe {} {}".format(file, os.path.splitext(file)[0]+".wav"))

for file in os.listdir(cwd):
    if file.endswith(".wav"):
        shutil.move(file, "WAVs")