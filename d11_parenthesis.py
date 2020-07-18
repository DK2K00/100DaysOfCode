def balance(paren):

    if(len(paren) % 2 != 0):
        print("Not balanced")
        return False

    checker = set([('(', ')'), ('[', ']'), ('{', '}')])
    starting = set("[{(")

    stack = []

    for i in paren:
        if(i in starting):
            stack.append(i)

        else:
            if(len(stack) == 0):
                return False

            p = stack.pop()

            if((p, i) not in checker):
                return False

    print("Balanced")
    return True

balance("[({({[[({})]]})})]")           