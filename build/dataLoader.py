import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from helpers.utils import load_file
from build.parsers.dataparser import DataParser
class DataLoader:
    def __init__(self):
        self.dataParser = DataParser()
    def load(self,data):        
        loaded_data = {}
        for d in data:
            try:
                loaded_data[d["name"]] = {}
                datafile =load_file(os.path.join("models",d["src"]))                
                datatemplate = load_file(os.path.join(parentdir,"templates","ModelTypes",d["type"]+".AuleModelType"))
                parsed_data_template = self.parseDataTemplate(datatemplate)                
                parsed_data_file = self.parseDataFile(datafile,parsed_data_template)                                
                loaded_data[d["name"]]["src"]= d["src"]
                loaded_data[d["name"]]["type"]= d["type"]
                loaded_data[d["name"]]["data"]= parsed_data_file
            except FileNotFoundError as e:
                print(e)
        return loaded_data
    def parseDataTemplate(self,datatemplate):
        scanned_tokens =self.dataParser.scantemplate(datatemplate)
        parsed_data_template = self.dataParser.parsetemplate(scanned_tokens)
        return parsed_data_template
    def parseDataFile(self,datafile,parsed_data_template):
        parsed_data_file = []        
        datafile = datafile.split("\n")
        for idx,line in enumerate(datafile):
            line = line.split(":")
            parsed_data_file.append({})
            for i,d in enumerate(parsed_data_template):
                if(type(parsed_data_template[d])==str):
                    if(parsed_data_template[d]=="alpha()"):
                        if(line[i].isalpha()):
                            parsed_data_file[idx][d] = line[i]
                        else:
                            print("Error: badly formatted Model definition File,Unexptected Parameters")
                            exit()
                elif(type(parsed_data_template[d]==list)):
                    assert(len(parsed_data_template)>0)
                    if(line[i] in parsed_data_template[d]):
                        parsed_data_file[idx][d] = line[i]
                    else:
                        print("Error: badly formatted Model definition File,Unexpected Parameters")
                        exit()
        return parsed_data_file
