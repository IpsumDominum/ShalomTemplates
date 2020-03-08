import jinja2
class TemplateBuilder:
    def __init__(self):
        pass
    def build(self,buildTree):
        pass
    def build_module(self,module,buildmode="soft"):
        if(buildmode =="soft" ):
            self.create_temp_file_structure(module["root"])
    def build_component(self,component,buildmode="soft"):
        pass    
    def create_temp_file_structure(self,module_root):
        if(os.path.isdir("tempbuild")):
            print("directory already exists")
        else:
            tokens = module_root.split("/")
            os.makedirs(os.path.join("tempbuild",*tokens))
