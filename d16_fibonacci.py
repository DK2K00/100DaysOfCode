#Functions to create fibonacci sequence

#Iteration
def fibo_i(n):
    if(n < 0):
        return False
    
    if(n == 1 or n == 0):
        return 0

    if(n == 2):
        return 1
    
    a = 0
    b = 1

    for i in range(2,n): 
        sum = a + b
        a = b
        b = sum

    return(sum)

fibo_i(9)

#Recursion
def fibo_r(n):
    if(n < 0):
        return False

    if(n == 1 or n == 0):
        return 0

    if(n == 2):
        return 1

    return(fibo_r(n-1) + fibo_r(n-2)) 

fibo_r(9)

#Memoization(Dynamic programming)
n = 9
cache = [None] * (n+1)

def fibo_d(n):
    if(n == 0 or n == 1):
        return n

    if(cache[n] != None):
        return(cache[n])

    cache[n] = fibo_d(n-1) + fibo_d(n-2)

    return(cache[n])

fibo_d(9)