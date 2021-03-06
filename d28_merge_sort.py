#Function to perform merge sort
def merge(arr):
    if(len(arr) > 1):
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        #Recursively called to split elements
        merge(left)
        merge(right)

        i = j = k = 0

        #Sorting elements
        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while(i < len(left)):
            arr[k] = left[i]
            i += 1
            k += 1

        while(j < len(right)):
            arr[k] = right[j]
            j += 1
            k += 1

    print("Merging:", arr)

#Testing
arr = [2,7,1,6,4,5,3]
merge(arr)
print(arr)        