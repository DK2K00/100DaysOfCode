def individual_sum(n):
    
    if(n == 0):
        return 0

    if(n == 1):
        return 1

    sum = 0

    sum += int(n % 10)
   # n = int(n / 10)    

    return(sum + individual_sum(n/10))

individual_sum(54321)
