#identifier

def isIdentifier(identifier):
    
    identifier = identifier.lower()
    
    if not identifier:
        return False

    if not identifier[0].isalpha():
        return False
    
    for s in identifier:
        if not (s.isalnum() or s == '_'):
            return False
        
    return True