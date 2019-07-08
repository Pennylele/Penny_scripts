import os, json, pprint, glob, shutil, sys
from zipfile import ZipFile
import simplejson as json

dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, sketches in os.walk("."):        
    for sketch in os.listdir(root):
        if sketch.endswith(".sketch"):
            base = os.path.splitext(sketch)[0]
            os.chdir(root)
            with ZipFile(sketch, 'r') as zip:
                zip.extractall(base+"_forTrans")  

            os.chdir(base+"_forTrans")
            shutil.rmtree("images")
            shutil.rmtree("previews")
            os.remove("user.json")
            os.remove("meta.json")

            for r, d, JSON in os.walk("."):
                for jsons in JSON:
                    print (jsons)
                    json_path = os.path.join(r, jsons)
                    #print(json_path)
                    j = open(str(json_path), mode="r+", encoding="utf-8")
                    obj = json.load(j)
                    j_pretty = open(str(json_path), mode="w", encoding="utf-8")
                    j_pretty.write(json.dumps(obj, indent=2, sort_keys=False))

            os.chdir(dir_path)