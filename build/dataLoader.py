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
        for d in data:
            try:
                datafile =load_file(os.path.join("shalomproject","data",d["src"]))
                datatemplate = load_file(os.path.join("templates","DataModels",d["type"]+".shalomDataModel"))
                parsed_data_template = self.parseDataTemplate(datatemplate)
                parsed_data_file = self.parseDataFile(datafile)
                print(datafile)
            except FileNotFoundError as e:
                print(e)
    def parseDataTemplate(self,datatemplate):
        scanned_tokens =self.dataParser.scan(datatemplate)
        parsed_data_template = self.dataParser.parse(scanned_tokens)
        return parsed_data_template
    def parseDataFile(self,datafile):
        parsed_data_file = {}
        return parsed_data_file
