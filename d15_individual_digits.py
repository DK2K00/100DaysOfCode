#Function to add individual digits of a given number using recursion
def individual_sum(n):
    
    if(n == 0):
        return 0

    if(n == 1):
        return 1

    sum = 0
    #Splitting individual digits
    sum += int(n % 10)   

    return(sum + individual_sum(n/10))

individual_sum(54321)
