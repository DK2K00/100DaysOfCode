def reverse(s):

    length = len(s)

    if(length <= 1):
        return(s)
    
    return(s[length-1] + reverse(s[0:length-1]))

reverse("helloworld")
