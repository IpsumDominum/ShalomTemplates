import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import save_file
from generate.gen_templates import *
from jinja2 import Template

def generate_component(componentName):
    """Component Generation"""    
    if(os.path.isdir(os.path.join("templates",componentName))):
        print("error: Component Already Exists")
    else:
        os.mkdir(os.path.join("templates",componentName))
        os.mkdir(os.path.join("templates",componentName,"src"))
        """Generate component"""
        save_file(os.path.join("templates",componentName,"src",componentName+".html"),"hi")
        save_file(os.path.join("templates",componentName,"src",componentName+".ts"),"hi")
        save_file(os.path.join("templates",componentName,componentName+".py"),"hi")
        print(componentName+"generated")
    template = Template(component_template)
    print(template.render(componentName="hi"))