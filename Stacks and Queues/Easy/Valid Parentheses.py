#20
def isValid(s):
    stack = []
    match = {
        '}':'{',
        ']':'[',
        ')':'('
    }

    for item in s:
        if item in match:
            if not stack or stack.pop() != match[item]:
                return False
        else:
            stack.append(item)
    # if stack is empty -> (not False): True
    # if stack is not empty -> (not True): False
    return not stack