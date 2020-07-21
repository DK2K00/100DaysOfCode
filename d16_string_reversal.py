#Function to reverse string using recursion
def reverse(s):

    #To determine length of string
    length = len(s)

    if(length <= 1):
        return(s)
    
    #Recursion
    return(s[length-1] + reverse(s[0:length-1]))

reverse("helloworld")
