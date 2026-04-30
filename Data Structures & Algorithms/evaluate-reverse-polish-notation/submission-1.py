import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(str(int(num1) + int(num2)))
                elif token == '-':
                    stack.append(str(int(num1) - int(num2)))
                elif token == '*':
                    stack.append(str(int(num1) * int(num2)))
                elif token == '/':
                    result = int(num1) / int(num2)
                    if result > 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                    stack.append(str(result))
            else:
                stack.append(token)
            print(stack)

        return int(stack[0])