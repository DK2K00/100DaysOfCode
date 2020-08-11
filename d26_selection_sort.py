#Function to perform selection sort
def selection(arr):
    min = 0
    for i in range(len(arr)):
        position = i
        min = position
        for j in range(position,len(arr)):
            if(arr[min] > arr[j]):
                min = j

        #To swap minimum value
        temp = arr[position]
        arr[position] = arr[min]
        arr[min] = temp

#Testing
arr = [2,1,5,3,4,6]
selection(arr)
print(arr)