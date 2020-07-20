#Function to continuously add numbers using recursion
def continuous_add(n):
    if(n == 0):
        return 0

    if(n == 1):
        return 1
    #Performimg
    return(n + continuous_add(n-1))

continuous_add(5)
