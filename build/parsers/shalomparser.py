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
    parsed = get_syntax_definition_from_grammar(string_toks,grammar)
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
        return token in Base_Tokens  
    else:
         return token
def get_syntax_definition_from_grammar(string_toks,grammar):
    """
    How it works:
    Go from each token of the grammar,
    Look at it's modifier(ie. if it is special, say *, then we are
    expecting it,or expecting the next token,which could be the nil token)
    expand it if it is not a 
    """
    parsed = []
    token_num = 0
    """
    TODO
    Need to hireachically expand the grammar
    At each level, keep track of expected
    next token. Continue if string token
    is valid.
    Also need to keep track of each level of 
    hireachy.
    Expanding each hirachy level completely
    and then returning to higher level, moving
    on to the next token.
    """
    expected = []
    current = ""
    DFA = DFA()
    idx = 0  
    construct_DFA_from_grammar(DFA,grammar,idx)  
    return parsed
def match_base_token(string_tok,grammar_tok):
    pass
"""
Recursively construct DFA from
grammar
"""
def construct_DFA_from_grammar(DFA,grammar,idx):
    for n,token in enumerate(get_tokens(grammar)):
        if(is_terminal(token)):
            if(token.modifier=="1"):
                #Add a connection to next state
                DFA.add_state(idx,{token:idx+1})
                idx +=1#To construct next state
            elif(token.modifier=="*"):
                #Add a connection to a loop state
                #The loop state should have a connection to next state
                DFA.add_state(idx,{token:idx+1,get_tokens(grammar)[n+1]:idx+2})
                #Next string to next state
                DFA.add_state(idx+1,{get_tokens(grammar)[n+1],idx+2})                
                idx +=2#Skip to next next state
            elif(token.modifier=="+"):
                #Add a connection to a state with self looping, as well
                #As connection to next state
                DFA.add_state(idx,{token:idx+1})
                DFA.add_state(idx+1,{token:idx+1,get_tokens(grammar)[n+1]:idx+2})
                idx +=2#Skip to next next state
        else:
            pass
            #construct_DFA_from_grammar(DFA,grammar,idx)
    return DFA