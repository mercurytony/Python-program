def has_multiple(string,char):
    char_present = False 
    for c in string:
        if c == char:
            if len(c + c) >= 2:
                return True
        else:
            char_present = True
    return False 
