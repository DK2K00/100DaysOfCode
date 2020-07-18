def total_checker_all(arr, tot):
    n = 0
    pairs = set()

    for i in arr:
        for j in arr:
            if(i + j == tot):
                if(i - j >= 0):
                    tut = (i, j)
                    pairs.add(tut)
                    n += 1
    
    print("Number pf pairs: ", n)
    print("Pairs are: ", pairs)

total_checker_all([0, 1, 2, 2, 3, 4], 4)



