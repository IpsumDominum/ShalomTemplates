import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,dasherize,capitalize
from build.parsers.componentparser import parsecomponent
class ComponentLoader:
    def __init__(self):
        pass
    def load(self,components):      
        templates = {}          
        for component in components:
            component_template = self.get_component_template(component["type"])
            templates[component["type"]] = component_template
        return templates
    def get_component_template(self,componentType):
        if componentType in os.listdir(os.path.join(parentdir,"templates","Components")):
            componentDescription = load_file([parentdir,"templates","Components",componentType,"description.shalomComponent"])                
            componentTemplate = parsecomponent(componentDescription)                                
            return componentTemplate
        else:
            print("component not found {}".format(componentType))
            exit()