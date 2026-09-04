class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push nums onto stack
        # when encounter math symbol -> pop num2 num1 off stack, num1-num2

        stack = []
        for tok in tokens:
            print("tok: ", tok)
            if tok.isnumeric() or len(tok) > 1:
                stack.append(int(tok))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                match tok:
                    case '+':
                        stack.append(num1 + num2)
                    case '-':
                        stack.append(num1 - num2)
                    case '*':
                        stack.append(num1 * num2)
                    case '/':
                        stack.append(int(num1 / num2))
            print(stack)

        return stack[0]