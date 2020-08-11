#Function to perform insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        current_val = arr[i]
        pos = i

        while(pos > 0 and arr[pos - 1] > current_val):
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = current_val

#Testing
arr = [2,3,1,6,4,5]
insertion_sort(arr)
print(arr)