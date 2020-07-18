def reversal(str):

    words = []
    spaces = [" "]
    n = 0
    
    while(n < len(str)):
        if(str[n] not in spaces):
            start = n

            while(n < len(str) and str[n] not in spaces):
                n += 1

            words.append(str[start:n])

        n += 1
    
    #print(" ".join(reversed(words)))
    for i in words[::-1]:
        print(i, end=" ")

reversal("Hello my name is DK")