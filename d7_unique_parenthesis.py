def unique(s):

    count = {}

    for i in s:
        if(i not in count):
            count[i] = 1

        else:
            print("Not unique")
            return False

    print("Unique")
    return True


unique("DK")