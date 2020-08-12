#Function to perform shell sort
def shell(arr):
    sublist = int(len(arr)/2)

    #To create gaps to perform sorting
    while(sublist > 0):
        for start in range(sublist):
            gap_insertion(arr,start,sublist)

        sublist = int(sublist / 2)

#To perform insertion sort for repective sublist
def gap_insertion(arr,start,gap):
    for i in range(start+gap, len(arr), gap):
        currentVal = arr[i]
        pos = i

        while(pos >= gap and arr[pos-gap] > currentVal):
            arr[pos] = arr[pos-gap]
            pos = pos - gap

        arr[pos] = currentVal

#Testing
arr = [2,1,4,3,5,7,6]
shell(arr)
print(arr)