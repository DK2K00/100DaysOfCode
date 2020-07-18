def total(arr):
    max_sum = current_sum = arr[0]

    for i in arr[1:]:
        current_sum = max(current_sum + i, i)

        max_sum = max(max_sum, current_sum)

    print(max_sum)
    return True

total([1,2,-1,3,4,10,10,-10,-1])