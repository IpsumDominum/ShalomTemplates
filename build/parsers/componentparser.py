from collections import namedtuple
import re
Depend = namedtuple("Depend",'type name')
Param = namedtuple("Param",'type name')
Defin = namedtuple("Defin",'file vars')
def parsecomponent(component):
    """Parse document,
    get result:
    dependencies:[dependencies list]
    what to feed into component templates
    buildleaf = {"templates":
    "example.html":["examplevariable","somedatalist"]
    }
    """    
    dependencies = []
    buildLeaf = {}
    """Sub parts"""
    depends = []
    params = []
    defins = []
    header = []
    state = "d"
    buffer = ""
    for ch in component:
        if(ch=="\n"):
            continue
        if(state=="d"):
            if(ch==";"):
                depends.append(buffer)
                buffer = ""
            elif(ch=="("):
                state = "p"
                header.append(buffer)
                buffer = ""
            else:
                buffer += ch
        elif(state=="p"):
            if(ch==","):
                params.append(buffer)
                buffer = ""
            elif(ch==")"):
                state="m"
            else:
                buffer +=ch
        elif(state=="m"):
            if(ch==";"):
                defins.append(buffer)
                buffer = ""
            elif(ch=="}"):
                state = "d"
            elif(ch=="{"):
                pass
            else:
                buffer +=ch
    dependencies = parseDepends(depends)
    buildLeaf["params"] = parseParams(params)
    buildLeaf["defins"] = parseDefins(defins)
    return buildLeaf,dependencies
def parseDepends(depends):
    parsed_depends = []
    for depend in depends:
        try:
            tokens = depend.split(" ")        
            tokensSecond = tokens[1].split(":")
            assert(len(tokens)==2 and
                tokens[0]=="depend" and 
                len(tokensSecond)==2)
            d_type = tokensSecond[0]
            d_name = tokensSecond[1]
            parsed_depends.append(Depend(d_type,d_name))
        except AssertionError:
            print("invalid formatting: '{}'".format(depend))
    return parsed_depends
def parseParams(params):
    parsed_params = []
    for param in params:
        param = param.replace(" ","")
        tokens = param.split(":")
        assert(len(tokens)==2)
        p_type = tokens[0]
        p_name = tokens[1]
        parsed_params.append(Param(p_type,p_name))
    return parsed_params
def parseDefins(defins):
    parsed_defins = []
    regex = re.compile(r"\s+|\"|\[|\]")
    for defin in defins:
        defin = regex.sub('',defin)
        tokens = defin.split("<-")
        assert(len(tokens)==2)
        def_file = tokens[0] 
        def_vars = tokens[1].split(",")
        parsed_defins.append(Defin(def_file,def_vars))
    return parsed_defins