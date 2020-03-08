def parse_structure(structure):
    """
    Parse the structure file and returns a representation of the 
    structure,
    which is a tree,
    Main -> Module -> components
    """
    parsed = structure
    for line in parsed:
        line = line.strip("\n")
    return parsed