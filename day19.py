'''
Given a postfix expression (also known as Reverse Polish Notation), your task is to evaluate the expression and return the result. The expression can contain integers and the four basic arithmetic operators +, -, *, and /. Assume that the input is always valid and the division operator performs integer division, truncating towards zero.
Input:
A string representing a postfix expression where operands and operators are separated by spaces.
The string contains only integers (both positive and negative) and the operators +, -, *, and /.
Output:
An integer representing the result of evaluating the postfix expression.
Examples:
Example 1
Input: "2 1 + 3 *"
Output: 9
Explanation: 
First, 2 and 1 are pushed onto the stack.
Encountering '+', 1 and 2 are popped, added to get 3, and pushed back onto the stack.
Then, 3 is pushed onto the stack.
Encountering '*', 3 and 3 are popped, multiplied to get 9, and pushed back onto the stack.
The final result is 9.
'''
def day19_sol(s):
    l = s.split()
    num = []
    oper = []
    operators = ['+','-', '*','/']
    for i in range(len(l)):
        if l[i] in operators:
            if l[i] == '*':
                num.append(num.pop()*num.pop())
            elif l[i] == '/':
                a = num.pop()
                num.append(num.pop()/a)
            elif l[i] == '+':
                num.append(num.pop()+num.pop())
            else:
                a = num.pop()
                num.append(num.pop()-a)
        else:
            num.append(int(l[i]))
    return int(num[0])
    
print(day19_sol("2 1 + 3 *"))
