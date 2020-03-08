import re
class DataParser:

    def __init__(self):
        self.regex = re.compile(r"\"+|\s+")
    def parse(self,scanned_tokens):
        parsed_data_template = {}
        found_definition = False
        """Assume definition Exists
        TODO: Check definition exists,
              Check syntax and other errors
        """
        default_types = ["string()","number()"]
        for item in scanned_tokens["definition"]:
            tokens = self.regex.sub("",item).split(":")                    
            assert(len(tokens)==2)
            def_name = tokens[0]
            def_type = tokens[1]
            if(def_type in default_types):
                parsed_data_template[def_name] = def_type
            else:
                """If not default type, then get 
                   definition from file definition
                   TODO:check file definition exists
                """
                parsed_data_template[def_name] = self.parse_type_definition(scanned_tokens[def_type])
        return parsed_data_template
    def parse_type_definition(self,filedefinition):
        type_def = []
        for item in filedefinition:
            type_def.append(self.regex.sub("",item))    
        return type_def
    def scan(self,datatemplate): 
        scanned_tokens = {}
        buffer = ""
        last_def = ""
        state = "closed"
        for ch in datatemplate:
            if(ch=="\n"):
                continue
            if(ch=="{" and state=="closed"):
                last_def = buffer
                state = "open"
                buffer = ""
            elif(ch=="}" and state=="open"):
                """Evaluate buffer, then append to datatemplate"""
                scanned_tokens[last_def] = []
                tokens = buffer.split(",")
                for token in tokens:
                    scanned_tokens[last_def].append(token)
                last_def = ""
                buffer=""
                state = "closed"
            else:
                buffer +=ch
        return scanned_tokens