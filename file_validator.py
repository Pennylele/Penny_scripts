import os, json, shutil


user = input("What file type do you want to validate?\n[yaml, json, android, or iOS]\n")

dir_path = os.path.dirname(os.path.realpath(__file__))

def validate_yaml(data):
    os.system("yamllint {}".format(data))

def validate_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

def validate_android(path):
    os.chdir(path)
    os.system("ruby {}".format('android_validator.rb'))


def validate_iOS(data):
    os.system("plutil -lint {}". format(data))


# Validate YAML files

JSONs = []
YAMLs = []
Android = []
iOS = []

yaml_extentions = ['yml', 'yaml']

for root, dirs, files in os.walk("."):
    for yaml in os.listdir(root):
        if yaml.endswith(tuple(yaml_extentions)):
            YAMLs.append(os.path.join(root, yaml).strip("./"))

    for jn in os.listdir(root):
            if jn.endswith(".json"):
                JSONs.append(os.path.join(root, jn))

    for ios in os.listdir(root):
        if ios.endswith(".strings"):
            iOS.append(os.path.join(root, ios).strip("./"))

    for xml in os.listdir(root):
        if xml.endswith(".xml"):
            file_path = os.path.join(root, xml)
            destination_path = os.path.dirname(os.path.abspath(file_path))
            shutil.copy('android_validator.rb', destination_path+"/android_validator.rb")

    for rb in os.listdir(root):
        if rb.endswith(".rb"):
            Android.append(os.path.dirname(os.path.join(root, rb)))



if user.lower() == 'yaml':
    validate_yaml(" ".join(YAMLs))
elif user.lower() == 'json':
    for jn in JSONs:
        j = open(jn, encoding='utf-8', mode="r+")
        print (jn + "==>" + str(validate_json(str(j.read()))))
elif user.lower() == 'android':
    Android.remove('.')
    for i in Android:
        validate_android(i)
        os.chdir(dir_path)
elif user.lower() == 'ios':
    validate_iOS(" ".join(iOS))
else:
    print ("Sorry, we don't have this option.. Please choose again.")