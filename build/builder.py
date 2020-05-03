from jinja2 import Template
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,write_file,capitalize,dasherize
class TemplateBuilder:
    def __init__(self,projectName):
        self.projectName = projectName
    def build(self,buildPipe):
        self.create_temp_file_structure()
        for item in buildPipe:
            """
            Template should be able to handle dependencies.
            Depending on the type of the template
            
            There are several types of templates
            -Component
                -needs routing
                -can depend on Data Module
                -can depend on Model Module
                -can depend on Form Module
            -Route Module
            -Data Module
                -needs API definition
            -Form Storage
                -depend on Data Module
                -depend on Model module
                -can depend on Component
                -append Form definition in form aggregation file
            """
            rendered = Template(load_file(item.src)).render(**item.data,componentName=item.componentName,capitalize=capitalize,dasherize=dasherize)
            write_file(rendered,item.destination)
    def create_temp_file_structure(self):
        if(os.path.isdir(os.path.join("build"))):
            pass
        else:
            os.mkdir(os.path.join("build"))
