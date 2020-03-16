import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file,dasherize,capitalize
from build.builder import TemplateBuilder
from build.dataLoader import DataLoader
from build.componentLoader import ComponentLoader
from collections import namedtuple
BuildItem = namedtuple("BuildItem",'src destination data componentName')
class Pipeline:
    def __init__(self,parsed,projectName):
        self.projectName = projectName
        self.template_root_path = os.path.join(parentdir,"templates","Components")   
        self.builder = TemplateBuilder(self.projectName)
        self.data_loader = DataLoader()
        self.component_loader = ComponentLoader()
        buildpipe = self.get_build_pipe(parsed)
        self.builder.build(buildpipe)
    """
        get_build_tree(parsed)
        @parsed - the parsed Structure From structure.shalom
        Traverse through the parsed structure,and build a buildtree
        to be used to handle file building and template etc.
    """
    def get_build_pipe(self,parsed):        
        data = self.data_loader.load(parsed["models"])
        componentTemplates = self.component_loader.load(parsed["components"])        
        self.check_dependencies(parsed)
        buildpipe = self.construct_build_pipe(parsed,data,componentTemplates)
        return buildpipe    
    def check_dependencies(self,buildTree):
        pass
    def construct_build_pipe(self,parsed,data,componentTemplates):
        build_pipe = []
        for component in parsed["components"]:
            assert len(component["params"])==len(componentTemplates[component["type"]]["params"])
            got_params = {}            
            for i,param in enumerate(component["params"]):
                if(data[param]["type"] == componentTemplates[component["type"]]["params"][i].type):
                    got_params[componentTemplates[component["type"]]["params"][i].name] = data[param]["data"]
                else:
                    print("Incompatible parameter types {} {}".format(data[param]["type"],componentTemplates[component["type"]]["params"][i].type))
                    exit()
            """After we know the parameter types are all fine"""
            for defin in componentTemplates[component["type"]]["defins"]:
                replaced_vars = {}
                for var in defin.vars:
                    replaced_vars[var] = got_params[var]
                build_src = os.path.join(self.template_root_path,component["type"],"src",defin.file)
                build_destination = os.path.join(os.getcwd(),self.projectName,"build",*component["root"].split("/"),dasherize(capitalize(component["name"])+capitalize(component["type"])),defin.file)
                build_pipe.append(BuildItem(build_src,build_destination,replaced_vars,component["name"]))
        return build_pipe
