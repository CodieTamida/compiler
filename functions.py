#Determine if identifier
def isIdentifier(identifier):
    #Convert all value to lower case
    identifier = identifier.lower()
    #Check if identifier is empty string
    if not identifier:
        return False
    #Check if the the beginning of identifier is a letter
    if not identifier[0].isalpha():
        return False
    #Check if all elements in identifier are letters,numbers, or underscore
    for s in identifier:
        if not (s.isalnum() or s == '_'):
            return False
    
    return True

# Determine if integer
def isInteger(integer):
    if not integer:
        return False
    ints = ['1','2','3','4','5','6','7','8','9','0']
    for s in integer:
        if s not in ints:
            return False
    return True