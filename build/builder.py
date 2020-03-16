from jinja2 import Template
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,write_file
class TemplateBuilder:
    def __init__(self,projectName):
        self.projectName = projectName
    def build(self,buildPipe):
        self.create_temp_file_structure()
        for item in buildPipe:
            rendered = Template(load_file(item.src)).render(**item.data,componentName=item.componentName)
            write_file(rendered,item.destination)
    def create_temp_file_structure(self):
        if(os.path.isdir(os.path.join(self.projectName,"build"))):
            pass
        else:
            os.mkdir(os.path.join(self.projectName,"build"))
