def checker(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            print(i, " is not present in the list")
            return False

    print("All numbers are present in the list")
    return True

checker([1,2,3,4,5], [4,2,1,3])