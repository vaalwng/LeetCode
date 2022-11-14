def isValidParentheses(s):
    """
    :type s: str
    :rtype: bool
    """

    # return if the string given is empty
    if len(s) == 0:
        return False

    # stack to be used to hold parenthesis, etc. in sequential order
    stack = []

    # iterate through the string
    for char in s:

        # if the current char is a OPEN parenthesis, bracket, or curly bracket add it to the stack
        if char in ['(', '[', '{']:
            stack.append(char)
        
        # otherwise
        else:

            # if stack is empty, return False
            if not stack:
                return False
            
            # take the top element from the stack
            curr = stack.pop()

            # if the current char is a CLOSED parenthesis, bracket, or curly bracket 
            # make sure the top element popped is its corresponding OPEN
            # otherwise, its not VALID
            if curr == '(':
                if char != ')':
                    return False
            if curr == '[':
                if char != ']':
                    return False
            if curr == '{':
                if char != '}':
                    return False
    
    # if stack has elements, then something doesn't have a matching
    if len(stack) != 0:
        return False
    
    return True


if __name__ == "__main__":
    s = "{()}"
    print(isValidParentheses(s))