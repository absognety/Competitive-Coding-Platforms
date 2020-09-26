#!/media/vikas/Data/Files/favpython/bin/python3

"""
Daily Coding Problem #163

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, 
write a program to evaluate it.

The expression is given as a list of numbers and operands. 
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, 
[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
should return 5, since it is equivalent to 
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

"""

def evaluate_postfix_exp(exp):
    stack = []
    d = 0
    while (d <= len(exp)-1):
        if exp[d] in ['+','-','/','*']:
            if (len(stack) != 0) and (len(stack) >= 2):
                opd1 = stack.pop()
                opd2 = stack.pop()
                res = eval('{}{}{}'.format(opd2,exp[d],opd1))
                stack.append(res)
        if isinstance(exp[d],int):
            stack.append(exp[d])
        d += 1
    assert len(stack) == 1,"re-check your solution"
    return stack[0]

print (evaluate_postfix_exp([5, 3, '+']))
print (evaluate_postfix_exp([15, 7, 1, 1, '+', 
                             '-', '/', 3, '*', 2, 1, 1, 
                             '+', '+', '-']))
print (evaluate_postfix_exp([2,3,1,'*','+',9,'-']))