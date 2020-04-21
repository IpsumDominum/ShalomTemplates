import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,print_error
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
            loaded = yaml.load(project_structure)
            project["name"]= loaded["Project Name"]
            parsed = self.structureParser.parse(loaded["Modules"])
            exit()
            project = {"name":"shalomproject","parsed":
                    {"components":[
                    {
                        "root":"src/app/billingModule",
                        "name":"rental",
                        "type":"formComponent",
                        "params":["rentalModel"]
                    },
                    {
                        "root":"src/app/billingModule",
                        "name":"rental",
                        "type":"formComponent",
                        "params":["rentalModel"]
                    },
                ],"models":[{
                    "name":"rentalModel",
                    "type":"StandardModel",
                    "src":"rental.auleModel"
                }]
                }}
        return project