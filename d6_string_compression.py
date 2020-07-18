def compress(s):

    length = len(s)
    n = 1
    i = 0

    if(length == 0):
        return False
    
    while(i < length):
        future = i + 1
        if(future != length and s[i] == s[future]):
            n += 1
            i += 1
            
        else:
            print(s[i] + str(n), end = "")
            n = 1 
            i += 1   
    return True

compress("AAAAAAaaaaaBBBBBBBBBBBBBBBBBBBBBBBBbbbbbbbbbbb")