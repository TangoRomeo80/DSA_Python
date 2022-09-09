def evalRPN(tokens):
    stack = [] # stack to store operands
    for token in tokens:
        #check if token is not an operator
        if token not in '+-*/':
            stack.append(int(token))
        else:
            #if operator then pop two operands from stack
            b = stack.pop()
            a = stack.pop()
            #perform operation and push result back to stack
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    return stack.pop()