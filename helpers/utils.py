import os
import re
def print_error(messageprimary,messagesecondary=""):
    CSI="\x1B["
    print(CSI+"31;40m" + messageprimary+ CSI + "0m")
    if(messagesecondary!=""):
        CSI="\x1B["
        print(CSI+"33;40m" + u"\u2588"+messagesecondary + CSI + "0m",end="")
        print("\n")
def dasherize(string):
    dasherized = ""
    first_cha = True
    for c in string:        
        if(len(re.findall("[A-Z]",c))>0):
            if(first_cha):
                dasherized+=c.lower()
                first_cha = False
            else:
                dasherized +="-" + c.lower()
        else:
            dasherized += c
    return dasherized
def load_file(path):
    if(type(path)==list):
        with open(os.path.join(*path),"r") as file:
                return file.read()
    else:
        with open(os.path.join(path),"r") as file:
                return file.read()
def print_invalid_usage():
        print("usage: python main.py build --filepath")
        print("                      generate --componentName")
def save_file(path,filecontent):
    with open(path,'w') as file:
        file.write(filecontent)
def capitalize(string):
        newstring = ""
        newstring += string[0].upper()
        newstring +=string[1:]
        return newstring