#!/usr/bin/env python

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
from build.buildpipline import *
from generate.genComponent import * 
from generate.gen_project import *
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
            """shalom build """            
            Pipeline()
            exit()
        elif(argv[1]=="new"):
            """shalom new --projectName"""
            if(len(argv)>2):
                projectName = argv[2]
                generate_new_project(projectName)
            else:
                projectName = prompt_project_name()
                generate_new_project(projectName)
            exit()
        elif(argv[1]=="help"):
            print_help()
    """If does not terminate early, print invalid usage"""
    print_usage()
if __name__ =="__main__":
    main()
