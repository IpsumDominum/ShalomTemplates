import re
from collections import namedtuple
Token = namedtuple("Token","string modifier")
Known_Tokens =  {
"<ComponentTemplateName>":r"<string>",
"<ComponentParams>":r"(<paramname><paramwithsep*>)",
"<paramname>":r"name=[\"<string>\"]",
"<paramwithsep>":r",<string>=[\"<string\"]",
"<ModelName>":r"<string>",
"<ModelTemplateName>":r"<string>",
}
Base_Tokens = ["<string>"]
"""
Valid Grammar definitions:
character(*or+) <grammardef(*or+)>
"""
def parse_from_grammar(string,grammar):
    tokens = get_tokens(grammar)
    expanded_tokens = expand_tokens(tokens)    
    #TODO:
    #Currently expanded tokens is an expanded expression of the Grammar, however we
    #Want abstract syntax tree to be returned and also modifiers to be considered.
    #Need to reimplement expand tokens.
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
def expand_tokens(tokens):
    #Given a list of tokens as input,
    #If any token in the list is a Known Token
    #Recursively,expand the known token definition.
    expanded = []
    for token in tokens:
        if(token.string in Known_Tokens):
            #Replace token with definition, if it is known
            meta_tokens = get_tokens(Known_Tokens[token.string])
            for expanded_item in expand_tokens(meta_tokens):
                expanded.append(expanded_item)
        else:
            if(is_token(token)):
                if(token.string in Base_Tokens):
                    expanded.append(token)
                else:
                    raise Exception("Token '{}' not in known tokens".format(token.string))
            else:
                #Some other syntax, carry on
                expanded.append(token)
    return expanded
def is_token(token):
    return token.string[0]=="<" and token.string[-1]==">"
