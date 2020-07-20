#Function to split string if sliced string is present in words list
def word_split(s, words):
    
    word_list = []
    i = j = 0

    #Traversing through each character
    for i in range(len(s)):
        for j in range(len(s)):

            #Making sure reverse slice is not done
            if(j <= i):
                pass

            if(s[i:j+1] in words):
                word_list.append(s[i:j+1])

    if(len(word_list) == 0):
        return False

    else:
        return word_list

#Testing
s = "goodmorningindiaandcanada"

words = ["good", "india", "and"]

word_split(s, words)