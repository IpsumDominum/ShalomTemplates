class TreeNode():
    def __init__(self,value="root",parent=None,modifier="1"):
        self.value = value
        self.leaves = []
        self.parent = parent
        self.modifier = modifier
        self.visited = False
    def add(self,token):
        if(is_terminal(token)):
            self.leaves.append(TreeNode(value=token.string,parent=self.value,modifier=token.modifier))
        else:
            tokens = expand(token.string)
            leafNode = TreeNode(value=token.string,parent=self.value,modifier=token.modifier)
            for tok in get_tokens(tokens):
                leafNode.add(tok)            
            self.leaves.append(leafNode)
        return
    def print(self,leaves):
        for leaf in leaves:
            print(leaf,end=" | ")
        print()
    def __str__(self):
        return " |{}| ".format(self.value)

class ParseTree:

    def __init__(self):
        self.root = TreeNode()
    def add(self,token):
        self.root.add(token)
    def __str__(self):
        return self.root.traverse("")
"""
Shalom parser is just a simple way to organize 
the context free grammar that is used
to define simple grammars of the
shalom definitions.
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import re
from collections import namedtuple
from build.parsers.DFA import DFA
Token = namedtuple("Token","string modifier")
StringToken = namedtuple("StringToken","tokendef tokenval")
ParsedBaseToken = namedtuple("ParsedBaseToken","name value")
ParsedToken = namedtuple("ParsedToken","name value")
Known_Tokens =  {
"<ComponentGrammar>":r"<ComponentTemplateName><ComponentParams>",
"<ModelGrammar>":r"<ModelName>:<ModelTemplateName>",
"<ComponentTemplateName>":r"<string>",
"<ComponentParams>":r"(<param><paramwithsep*>)",
"<param>":r"<string>=[\"<string>\"]",
"<paramwithsep>":r",<string>=[\"<string>\"]",
"<ModelName>":r"<string>",
"<ModelTemplateName>":r"<string>",
}
Base_Tokens = ["<string>"]
"""
Valid Grammar definitions:
character(*or+) <grammardef(*or+)>
"""
def parse_from_grammar(string,grammar):    
    """
    @return parsed
    parsed is a dictionary which might look like this:
    parsed = [
        ParsedToken("<ComponentParams>",value=
        [
            ParsedToken("<paramname>",value=[
                ParsedBaseToken("<string>",value="somevalue")
            ]),
            ParsedToken("<paramwithsep>",value=[]),
            ParsedToken("<paramwithsep>",value=[]),
            ParsedToken("<paramwithsep>",value=[]),
            ParsedToken("<paramwithsep>",value=[])
        ]
        ),
        ParsedToken("<ComponentTemplateName>",value=[

        ]
        )
    ]
    """    
    tokens = get_tokens(grammar)
    string_toks = string_to_token(string)
    parse_tree = get_parse_tree_from_grammar(grammar)
    parsed = traverse_parse_tree(parse_tree)
    return parsed
def string_to_token(string):
    tokens = []
    string_started = False
    string_temp = ""
    for c in string:
        if(string_started==True):
            if(not c.isalpha()):
                string_started = False
                tokens.append(StringToken("<string>",string_temp))
                tokens.append(StringToken("<sep>",c))
                string_temp = ""
            else:
                string_temp +=c
        elif(string_started==False):
            if(c.isalpha()):
                string_started = True
                string_temp+=c
            else:
                tokens.append(StringToken("<sep>",c))
    return tokens
        
def get_tokens(grammar_def):
    #Temporary solution, want to use raw strings for now
    #to get better syntax highlighting, in the future
    #backslash special characters should be defined...
    grammar_def = grammar_def.replace("\\","")
    tokens = []
    temp = ""
    expecting_start = True
    specials = ["*","+"]
    special_temp = "1"
    for c in grammar_def.replace(" ",""):        
        if(expecting_start==True):
            #expecting start character <
            if(c=="<"):
                temp+= c
                expecting_start = False
            elif(c in specials):
                if(special_temp=="1"):
                    special_temp = c
                else:
                    raise Exception("Invalid syntax {}".format(grammar_def))
            else:
                #If we have special modifiers to the token
                #If we don't, assume only one is wanted
                tokens.append(Token(c,special_temp))
                special_temp = "1"
        elif(expecting_start==False):            
            if(c==">"):
                #expecting end character >
                temp+= c
                expecting_start = True
                #If we have special modifiers to the token
                #If we don't, assume only one is wanted
                tokens.append(Token(temp,special_temp))
                temp = ""
                special_temp = "1"
            elif(c in specials):
                #if c is a special modifier (* or + etc)
                if(special_temp=="1"):
                    special_temp = c                                
                else:
                    raise Exception("Invalid syntax {}".format(grammar_def))
            else:
                temp+=c
    return tokens
def expand_token(token):
    #Given a Known token, expand it.
    expanded = []
    return expanded
def is_token(token):
    return token.string[0]=="<" and token.string[-1]==">"
def is_terminal(token):    
    if is_token(token):
        return token.string in Base_Tokens  
    else:
        return token
def get_parse_tree_from_grammar(grammar):
    """
    How it works:
    Go from each token of the grammar,
    Look at it's modifier(ie. if it is special, say *, then we are
    expecting it,or expecting the next token,which could be the nil token)
    expand it if it is not a 
    """
    parse_tree = ParseTree()
    for token in get_tokens(grammar):
        parse_tree.add(token)
    #print(parse_tree)
    #exit()
    return parse_tree
def traverse_parse_tree(string_toks):
    pass
def expand(token):
    if(token in Known_Tokens):
        return Known_Tokens[token]

        