"""Shalom, Template generator for the web

Uses Jinja

Overlay Structure:
[
    parse a structure description language
]
->
[
    Project Abstraction Graph
]
->
[
    
]
Template Definition ->
[
    
]
"""
from sys import argv
import os
from helpers.utils import *
from build.structureparser import *
from build.buildpipline import *
from generate.genComponent import * 
import shutil

template = """#This is an Aule Template, Run "python auleschematics generate" to generate
    {"modules":{
            "example-modules":{
                "example-module":{#note the difference is one is a collection the other is a module
                    "settings":{
                        "routing":True
                    },
                    "components":{
                        "example-component":{
                            "guard":False
                        }
                    }
                }
            }
        }
    }
"""
def main():
    if(len(argv)>1):
        if(argv[1]=="build"):
            """shalom build --filepath"""
            if(len(argv)>2):
                filepath = argv[2]
                #structureFile = load_file(filepath)
                #parsed = parse_structure(structureFile)
                parsed ={"components":[
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
                }
                Pipeline(parsed,"shalomproject")
                exit()
        elif(argv[1]=="generate"):
            """shalom generate --componentName"""
            if(len(argv)>2):
                componentName = argv[2]
                generate_component(componentName)
            exit()
    """If does not terminate early, print invalid usage"""
    print_invalid_usage()
if __name__ =="__main__":
    main()