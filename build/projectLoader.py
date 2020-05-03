import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,print_error,print_info
from build.parsers.structureparser import StructureParser
import yaml
class ProjectLoader:
    def __init__(self):
        self.structureParser = StructureParser()
    """
    Loads Project,
    First check if the current directory contains project.shalom file
    """
    def load_project(self):        
        #Check if the directory contains project.shalom
        project = {}        
        if not os.path.isfile("project.yaml"):
            print_error("Error:","'project.yaml' file not found in current directory. No project found here.")
            exit()
        else:
            project_structure = load_file("project.yaml")            
            loaded = yaml.load(project_structure,Loader=yaml.FullLoader)
            _ = self._check_valid_structure(loaded)            
            project["name"]= loaded["Project Name"]
            parsed = self.structureParser.parse(modules=loaded["Modules"],models=loaded["Models"])            
            project["parsed"] = parsed
        return project
    def _check_valid_structure(self,structure):
        for check in["Project Name","Modules","Models"]:
            if check not in structure:
                print_error("Error","{}'{}'{} Not found in structure definitions. Please follow the following standard format:".format('\033[95m',check,'\033[93m'))
                print_info("","""
                Project Name: xxx
                Modules:
                    Module1:
                        Componenta
                        Componentb
                    Module2:
                        Componentc
                Models:
                    ModelFoo
                    ModelBar
                """.replace(check,"{}{}{}{}".format('\033[95m',check,'\033[0m','\033[94m')))
                exit()
            else:
                pass
        return None