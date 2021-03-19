def isValid(s):
    if len(s) < 2:
        return False
    stack = []
    open = '(', '{', '['
    close = ')', '}', ']'
    openClose = {'(':')', '{':'}', '[':']'}  
    for i in s:
        print(stack)
        if i in open:
            stack.append(i)
        elif i in close:
            if len(stack)==0: 
                return False
            x = stack.pop()
            if openClose[x] != i:
                return False
    return len(stack) == 0

print(isValid(")(("))