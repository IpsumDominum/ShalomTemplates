import os
import re
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
class bcolors:
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def print_info(messageprimary,messagesecondary=""):
    if(messageprimary!=""):
        print(f"{bcolors.HEADER}"+messageprimary+f"{bcolors.ENDC}",end="")
    if(messagesecondary!=""):
        print(f"{bcolors.OKBLUE}"+messagesecondary+f"{bcolors.ENDC}")
def print_warning(messageprimary,messagesecondary=""):
    if(messageprimary!=""):
        print(f"{bcolors.HEADER}"+messageprimary+f"{bcolors.ENDC}",end="")
    if(messagesecondary!=""):
        print(f"{bcolors.OKBLUE}"+messagesecondary+f"{bcolors.ENDC}")
def print_error(messageprimary,messagesecondary=""):
    if(messageprimary!=""):
        print(f"{bcolors.FAIL}"+messageprimary+f"{bcolors.ENDC}",end="")
    if(messagesecondary!=""):
        print(f"{bcolors.HEADER}"+messagesecondary+f"{bcolors.ENDC}")
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
def prompt_project_name():
    print_info("Initiate new project","what is your project's name:")
    print(">",end="")
    name = input()
    return name
def load_file(path):
    if(type(path)==list):
        with open(os.path.join(*path),"r") as file:
                return file.read()
    else:
        with open(os.path.join(path),"r") as file:
                return file.read()
def write_file(towrite,path):
        if(not os.path.isdir(os.path.split(path)[0])):
                os.makedirs(os.path.split(path)[0])
        print_info("~Wrote ",path)
        with open(path,"w") as file:
                file.write(towrite)
def print_usage():
    print_version()
    print_info("usage: st build\n")
    print_info("          new","\n")
def print_help():
    pass
def print_version():
    from meta import NAME, VERSION
    print(f"{bcolors.BOLD}{bcolors.OKGREEN}"+ NAME + " v"+VERSION + f"{bcolors.ENDC}")
def save_file(path,filecontent):
    with open(path,'w') as file:
        file.write(filecontent)
def capitalize(string):
        newstring = ""
        newstring += string[0].upper()
        newstring +=string[1:]
        return newstring