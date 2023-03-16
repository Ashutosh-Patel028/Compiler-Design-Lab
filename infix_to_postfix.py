#Given a expression convert to postfix notation

OPERATORS = set(['+', '-', '*', '/', '(', ')','='])
PRI = {'=': 0,'+': 1, '-': 1, '*': 2, '/': 2}  #operator priority


def infix_to_postfix(formula):
    
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output




expres = input("INPUT THE EXPRESSION: ")
# pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
# print(list(pos))