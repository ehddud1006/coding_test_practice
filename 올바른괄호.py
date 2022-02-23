def check(s) :
    stack = []
    for w in s :
        if len(stack)>0 and stack[-1] == "(" and w == ")" :
            stack.pop()
        else :
            stack.append(w)

    if len(stack) == 0 :
        return True
    else :
        return False


def solution(s):
    return check(s)