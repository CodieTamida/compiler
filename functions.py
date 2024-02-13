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

def isInteger(integer):
    if not integer:
        return False
    ints = ['1','2','3','4','5','6','7','8','9','0']
    for s in integer:
        if s not in ints:
            return False
    return True