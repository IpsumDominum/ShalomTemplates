import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,dasherize,capitalize
from build.parsers.componentparser import parsecomponent
from build.builder import TemplateBuilder
from build.dataLoader import DataLoader
class Pipeline:
    def __init__(self,parsed):
        self.builder = TemplateBuilder()
        self.data_loader = DataLoader()
        buildpipe = self.get_build_pipe(parsed)
        self.builder.build(buildpipe)
    """
        get_build_tree(parsed)
        @parsed - the parsed Structure From structure.shalom
        Traverse through the parsed structure,and build a buildtree
        to be used to handle file building and template etc.
    """
    def get_build_pipe(self,parsed):
        #print(parsed)
        self.check_dependencies(parsed)
        data = self.data_loader.load(parsed["models"])
        build_Pipe =[
            {"directory":"Components/formComponent/src/formComponent.html",
            "variables":[]},
        ]
        return 0,0
#buildLeaves,dep = self.get_build_component(component,module["components"][component])        
    def get_build_component(self,componentType,component):                
        buildLeaves = {}
        dependencies = []
        if componentType in os.listdir(os.path.join("templates","Components")):
            try:
                componentDescription = load_file(["templates","Components",componentType,"description.shalomComponent"])
                buildLeaf,dep = parsecomponent(componentDescription)                
                dependencies.append(dep)                
                buildLeaves[dasherize(component["name"]+capitalize(componentType))] = buildLeaf
            except Exception as e:
                print(e)
                #print("description file not found...Bad Component definition")
            return buildLeaves,dependencies
        else:
            print("component not found {}".format(componentType))
    def check_dependencies(self,buildTree):
        pass
    