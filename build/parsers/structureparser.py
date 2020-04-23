import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
"""
Expected Parse Result
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
"""
from build.parsers.shalomparser import parse_from_grammar
class StructureParser:
    def __init__(self):
        self.componentGrammar = "<ComponentGrammar*>"
        self.modelGrammar = "<ModelGrammar*>"
    def parse(self,modules,models):
        result = {"components":[],"models":[]}
        #------Parse Components and Models------
        for m in modules:
            parsed = parse_from_grammar(modules[m],self.componentGrammar)
            result["components"].append(parsed)
        result["models"] = parse_from_grammar(models,self.modelGrammar)
        #------Checks semantcs-----
        self.check_semantics(result)
        return result
    def check_semantics(self,result):
        #Checks dependency etc.
        pass