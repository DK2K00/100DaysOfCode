def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    count = {}

    for i in str1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in str2:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1

    for i in count:
        if(count[i] != 0):
            print("Not an anagram")
            return False

    print("Anagram")
    return True

str1 = "hello"
str2 = "lehlo"

anagram(str1, str2)