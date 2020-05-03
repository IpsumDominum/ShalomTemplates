# ShalomTemplates
Based on Jinja2, <br>
Usage: <br>
```
st new --projectname
```
```
st build
```

Logic for parser (To be transferred to documentation)



```
    Here goes the logic:

    If the leaf is a terminal leaf,
    check on string_toks, if string_toks
    has next item corresponding,
    then register that item's value and form
    ParsedBaseToken().
    If the leaf has modifier "*":
        We keep checking and increasing idx
        until we find False,then we roll back idx
        Or until we find end of line. Then terminate 
        with True
        If we find False initially we can return True too,
        since * is optional.
    If the leaf has modifier "+":
        We keep checking and increasing idx
        until we find False,then we roll back idx
        Or until we find end of line. Then terminate 
        with True
    otherwise
        We check the next token in string,
        if it matches expected then we return True
        otherwise False

    If the leaf is not a terminal leaf:
        Then we expand it recursively.
        The result of the recursive expansion:
        Concretely for intuition,
        as an example:
        at the lowest level:
        We have    <token>
                    |   |
                    t1 <token2>
        Where <> denotes non-terminal leaf
        and no brackets otherwise.

        Here if t1 returns True,
        we check <token2>
        if <token2> also returns True
        our token accepted, and we
        return with forwarded idx
    If the <token> has modifier *:
        If the leaf has modifier "*":
        We keep checking and increasing idx
        until we find False,then return parsed and True
        If we find False initially we can return True too,
        since * is optional.
    If the <token> has modifier +:
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
    If the <token> has modifier 1:
        return True if match
        False if no match

    End Cases:
        There are a few cases to 
        consider.
        1.All of the expected Strings are
        found, and we didn't reach the 
        <nil> token, we just check if 
        the token is in fact a <nil> token,
        if so, we accept the whole parsed,
        otherwise we reject.

        2.Parse tree haven't been finished
        traversing, but the string has been
        exhausted. In the case the <nil>
        token will be rejected, leading
        to the rejection of the whole tree.

        3.In the case of the token which is
        supposed to reject <nil> being a *
        modifier token. If the * modifier
        is in the middle of the parse tree
        then the next should hopefully
        reject.
        Otherwise if it is in the end,
        we don't mind, it's still
        a valid accepted string by
        the grammar.
        
        4.If at any case unknown token
          is found, just terminate.
          This is the issue again of the
          grammar writing person. (me)

    Note:
    The case where t1 is <string*>
    and <token2> is also say <string>
    Will certainly cause a problem.
    So it is to be avoided in the
    grammar definition. 
    Hence this is not a fully 
    function parser for context
    free grammar.(not even regular
    languages) (obviously 
    since it does not support the
    "or" operator, "|", or
    aUb "union" operation)
    This parser is meant for a 
    quick and easy solution to 
    my own use in implementing 
    simple language definitions
    for data files.

```