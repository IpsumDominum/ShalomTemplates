class TreeNode():
    def __init__(self,value=None,parent=None,modifier="1"):
        self.value = value
        self.leaves = []
        self.parent = parent
        self.modifier = modifier
        self.visited = False
    def add(self,token):
        if(is_terminal(token)):
            self.leaves.append(TreeNode(value=token,parent=self.value,modifier=token.modifier))
        else:
            tokens = expand(token.string)
            leafNode = TreeNode(value=token,parent=self.value,modifier=token.modifier)
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
        return str(self.root)
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

Token = namedtuple("Token","string modifier")
StringToken = namedtuple("StringToken","tokendef tokenval")
ParsedBaseToken = namedtuple("ParsedBaseToken","name value")
ParsedToken = namedtuple("ParsedToken","name values")
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
    parse_tree = get_parse_tree_from_grammar(grammar)
    parsed = get_parsed(string.replace(" ",""),parse_tree)
    parsed = beautify_parsed(parsed)
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
    if(string_started):
        tokens.append(StringToken("<string>",string_temp))
    tokens.append(StringToken("<nil>",""))
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
    return parse_tree
def get_parsed(string,parse_tree):
    string_toks = string_to_token(string)
    parsed = []
    idx = 0
    for leaf in parse_tree.root.leaves:
        p_parsed,flag,_ = traverse_parse_tree(string_toks,leaf,idx)
        if(flag==True):
            parsed.append(p_parsed) #p_parsed = partially parsed
        elif(flag==False):
            raise(SyntaxError("Invalid syntax {}".format(string)))
    return parsed
def traverse_parse_tree(string_toks,leaf,idx):   
    parsed = []
    tempidx = idx #temp idx is used for rolling back
    """
    Token = namedtuple("Token","string modifier")
    StringToken = namedtuple("StringToken","tokendef tokenval")
    ParsedBaseToken = namedtuple("ParsedBaseToken","name value")
    ParsedToken = namedtuple("ParsedToken","name values")
    """
    if(is_terminal(leaf.value)):
        #If the leaf is a terminal token        
        if(leaf.value.modifier=="*"):
            """
            If the leaf has modifier "*":
            We keep checking and increasing idx
            until we find False,then return parsed and True
            If we find False initially we can return True too,
            since * is optional.
            """            
            while(True):
                if(string_toks[tempidx].tokendef==leaf.value.string):                    
                    #If match                    
                    parsed.append(ParsedBaseToken(leaf.value.string,string_toks[tempidx]))
                    tempidx +=1
                    idx +=1
                else:
                    #If no match                    
                    return parsed,True,idx
        elif(leaf.value.modifier=="+"):
            """
            we will return False if no match,
            True if match, and append
            until False is found.
            Again there is the problem of 
            <string*> to <string*>
            or <string+> to <string+>
            and similar.
            So the person writing the grammar
            has to consider that.
            And in fact that should be an 
            error in the parse_tree to catch
            "bad" grammar definitions which
            are impossible to parse.
            """
            if(string_toks[tempidx].tokendef==leaf.value.string):
                #If match                    
                parsed.append(ParsedBaseToken(leaf.value.string,string_toks[tempidx]))
                tempidx +=1
                idx +=1
                while(True):
                    if(string_toks[tempidx].tokendef==leaf.value.string):
                        #If match                    
                        parsed.append(ParsedBaseToken(leaf.value.string,string_toks[tempidx]))
                        tempidx +=1
                        idx +=1
                    else:
                        #If no match on + token
                        return parsed,True,idx
            else:
                #If no match on first token
                return parsed,False
        elif(leaf.value.modifier=="1"):
            """
            return True if match
            False if no match
            """
            if(string_toks[tempidx].tokendef=="<sep>"):
                if(string_toks[tempidx].tokenval==leaf.value.string):
                    #If match                    
                    parsed.append(ParsedBaseToken(leaf.value.string,string_toks[tempidx]))
                    tempidx +=1
                    idx +=1                
                    return parsed,True,idx
                else:
                    #If no match on first token
                    return parsed,False,idx
            elif(string_toks[tempidx].tokendef==leaf.value.string):
                #If match                    
                parsed.append(ParsedBaseToken(leaf.value.string,string_toks[tempidx]))
                tempidx +=1
                idx +=1                
                return parsed,True,idx
            else:                
                #If no match on first token
                return parsed,False,idx
        else:
            raise(Exception("Invalid modifier in parser found :{}"\
                .format(leaf.value.modifier)))
            #This should technically not be called, but it's good 
            #practice to raise exceptions on failure cases anyway
    else:
        #If the leaf is not a terminal token
        if(leaf.value.modifier=="*"):
            """
            We keep checking and increasing idx
            until we find False,then return parsed and True
            If we find False initially we can return True too,
            since * is optional.
            Token = namedtuple("Token","string modifier")
            StringToken = namedtuple("StringToken","tokendef tokenval")
            ParsedBaseToken = namedtuple("ParsedBaseToken","name value")
            ParsedToken = namedtuple("ParsedToken","name values")
            """            
            while(True):
                r_flag = True #result flag
                temp_values = []#prepared parent values                
                #For each leaf we expand
                for p_leaf in leaf.leaves:
                    t_parsed,t_flag,t_idx = traverse_parse_tree(string_toks,p_leaf,tempidx)                    
                    #Expand leaf may be good or not good.
                    if(t_flag==True):
                        #If leaf is good
                        temp_values += t_parsed #LIST CONCATENATION HERE!!!Add to the parent prepared earlier
                        tempidx = t_idx #only update tempidx here so we can roll back
                    else:
                        #If leaf is not good :P The parent is not accepted either.
                        r_flag = False
                        break                
                if(r_flag==True):
                    parsed.append(ParsedToken(leaf.value,temp_values))
                else:
                    break
            if(r_flag==True):
                idx = tempidx 
                return parsed,True,idx
            elif(r_flag==False):
                idx = tempidx 
                return parsed,True,idx

        elif(leaf.value.modifier=="+"):
            """
            we will return False if no match,
            True if match, and append
            until False is found.
            Again there is the problem of 
            <string*> to <string*>
            or <string+> to <string+>
            and similar.
            So the person writing the grammar
            has to consider that.
            And in fact that should be an 
            error in the parse_tree to catch
            "bad" grammar definitions which
            are impossible to parse.
            """
            r_flag = True #result flag
            temp_values = []#prepared parent values
            #Check for all the leaves.
            for p_leaf in leaf.leaves:
                t_parsed,t_flag,t_idx = traverse_parse_tree(string_toks,p_leaf,tempidx)
                #Expanded Leaf may be rejected or not
                if(t_flag==True):
                    #If leaf accepted
                    temp_values += t_parsed #LIST CONCATENATION HERE!!!Add accepted leaf results to the parent ParsedToken
                    tempidx = t_idx #only update tempidx here so we can roll back                    
                else:
                    #If leaf is not good :P The parent is not accepted either.
                    tempidx = idx #roll back :( Seek cover, mission aborted Meow
                    r_flag = False
                    break
            if(r_flag==True):
                #Found once (First guy is accepted)
                parsed.append(ParsedToken(leaf.value,temp_values))#We append the one we found
                idx = tempidx #Set idx to temp idx ;) (smiling for now)                
                while(True):
                    r_flag = True #Variable reuse??Seems like not good practice, ironically actually the intention is that it is here to make the code a bit more readible (lol, readible,haha)..Also this comment is getting out of town.
                    #Then we effectively enter * mode
                    #Expecting 0 or more of the token
                    #We'll check all it's children, recursively seeing if they
                    #all are accepted. We only accept the parent if all the children are accepted
                    #And we append the children values to the parent's values
                    temp_values = []#prepared parent token values
                    #For each leaf we expand
                    for p_leaf in leaf.leaves:
                        t_parsed,t_flag,t_idx = traverse_parse_tree(string_toks,p_leaf,tempidx)
                        #Expanded Leaf can be good or bad
                        if(t_flag==True):
                            #If leaf is good
                            temp_values += t_parsed #LIST CONCATENATION HERE!!!Append leaf result to the parent token values
                            tempidx = t_idx #only update tempidx here so we can roll back
                        else:
                            #If leaf is bad, then parent is rejected too
                            tempidx = idx #roll back :( Seek cover, mission aborted Meow
                            r_flag = False
                            break
                    if(r_flag==True):
                        parsed.append(ParsedToken(leaf.value,temp_values))
                    else:
                        break
                if(r_flag==True):
                    #This case only appears when we exhausted all the leaves, and 
                    #They were all of the type of the token which had the 
                    #modifier "+", the one we been looking for all along.
                    idx = tempidx
                    return parsed,True,idx
                elif(r_flag==False):
                    #Take all we found and return.
                    idx = tempidx #We don't roll back here.
                    return parsed,True,idx
            else:
                #If not even once is found, mission aborted :(
                return parsed,False,idx
        elif(leaf.value.modifier=="1"):         
            """
            return True if match
            False if no match
            """
            r_flag = True #result flag
            temp_values = []
            #Check all the leaves            
            for p_leaf in leaf.leaves:                                                
                t_parsed,t_flag,t_idx = traverse_parse_tree(string_toks,p_leaf,tempidx)                
                #Expanded leaf result may be good or bad
                if(t_flag==True):
                    #If result is good
                    temp_values += t_parsed #LIST CONCATENATION HERE!!!Add to parent.values
                    tempidx = t_idx #only update tempidx here so we can roll back                    
                else:
                    #If result is bad, we reject parent too
                    tempidx = idx #roll back :( Seek cover, mission aborted Meow
                    r_flag = False
                    break            
            if(r_flag==True):
                #All leaves are accepted, we accept parent too.
                parsed.append(ParsedToken(leaf.value,temp_values))
                idx = tempidx         
                return parsed,True,idx
            elif(r_flag==False):
                #There was something wrong with the leaves :(
                return parsed,False,idx
        else:
            raise(Exception("Invalid modifier in parser found :{}"\
                .format(leaf.value.modifier)))
            #This should technically not be called, but it's good 
            #practice to raise exceptions on failure cases anyway
def expand(token):
    if(token in Known_Tokens):
        return Known_Tokens[token]

def beautify_parsed(parsed):
    #By beautify we mean we put our parsed into a dictionary
    parsed_list= []
    for item in parsed[0]:
        if(type(item)== type(ParsedBaseToken("None","None"))):
            if(item.value.tokendef!="<sep>"):
                parsed_list.append({item.name:item.value.tokenval})
        elif(type(item)== type(ParsedToken("None","None"))):
            parsed_list.append({item.name.string:expand_parsed_item(item.values)}) #Recursion
    return parsed_list
    
def expand_parsed_item(parsed_item):
    #It's the same as the above function, but why not 
    #separate them so it's a tiny bit more readable.
    parsed_list = []
    for item in parsed_item:
        if(type(item)== type(ParsedBaseToken("None","None"))):
            if(item.value.tokendef!="<sep>"):
                parsed_list.append({item.name:item.value.tokenval})
        elif(type(item)== type(ParsedToken("None","None"))):            
            parsed_list.append({item.name.string:expand_parsed_item(item.values)}) #Recursion
    return parsed_list