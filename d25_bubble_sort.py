#Funvtion to perform bubble sort
def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

#testing
arr = [2,1,4,3,6,5]
bubble(arr)
print(arr)