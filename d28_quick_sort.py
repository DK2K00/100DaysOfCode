#Function to perform quick sort
def quick_sort(arr):
    sort_help(arr,0,len(arr)-1)

def sort_help(arr,first,last):
    if(first < last):
        splitpt = partition(arr,first,last)

        sort_help(arr,first,splitpt-1)
        sort_help(arr,splitpt+1,last)

def partition(arr,first,last):
    pivot = arr[first]
    left = first+1
    right = last

    done = False

    while(not done):
        while(left <= right and arr[left] <= pivot):
            left += 1

        while(right >= left and arr[right] >= pivot):
            right -= 1

        if(right < left):
            done = True

        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return(right)

#Testing
arr = [2,1,7,4,5,6,3]
quick_sort(arr)
print(arr)