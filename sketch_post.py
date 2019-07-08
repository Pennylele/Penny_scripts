import os, zipfile, shutil



for file in os.listdir('.'):
    if file.endswith (".sketch"):
        base = os.path.splitext(file)[0]
        with zipfile.ZipFile(file, 'r') as zip:
            zip.extractall(base)

        for folders in os.listdir("."):
            if folders.startswith(base+"_"):
                print(folders)
                os.system("ditto {} {}".format(folders, base))
                os.system("ditto {} {}".format(base, folders))
                os.chdir(folders)

                zipf = zipfile.ZipFile(base + '.sketch', 'w', zipfile.ZIP_DEFLATED)
                for root, dirs, files in os.walk("."):
                    for file in files:
                        fullPath = os.path.join(root, file)
                        zipf.write(fullPath)
                zipf.close()

                os.chdir("..")

