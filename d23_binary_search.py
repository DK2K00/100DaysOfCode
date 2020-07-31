#Function that performs binary search recursively
def binary(arr, num):
    start = 0
    end = len(arr) - 1
    flag = False

    while(start <= end and not flag ):
        mid = (start + end) // 2

        if(arr[mid] == num):
            flag = True
        
        else:

            if(num < arr[mid]):
                end = mid - 1
 
            else:
                start = mid + 1
                
    return flag

#Testing
arr = [1,2,3,4,5]
binary(arr,5)

#Function that performs binary search recursively
def rec_binary(arr, num):
    if(len(arr) == 0):
        return False

    else:
        mid = len(arr) // 2

        if(arr[mid] == num):
            return True

        if(num < arr[mid]):
            return rec_binary(arr[:mid], num)

        else:
            return rec_binary(arr[mid:], num)

#Testing
rec_binary(arr,5)