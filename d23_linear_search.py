#Function to perform linear search recursively
def linear(arr, num, i = 0):
    flag = False

    while(i < len(arr)):
        if(arr[i] == num):
            flag = True
            return flag

        else:
            i += 1
            return linear(arr, num, i)

    return flag

arr = [1,2,3,4,5]
linear(arr, 3)