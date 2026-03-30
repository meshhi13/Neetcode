class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while tokens:
            print(tokens)
            if tokens[0] in ["+", "-", "*", "/"]:
                y = stack.pop()
                x = stack.pop()

                if tokens[0] == "+":
                    tokens.pop(0)
                    tokens.insert(0, x + y) 
                elif tokens[0] == "-":
                    tokens.pop(0)
                    tokens.insert(0, x - y) 
                elif tokens[0] == "*":
                    tokens.pop(0)
                    tokens.insert(0, x * y) 
                elif tokens[0] == "/":
                    tokens.pop(0)
                    tokens.insert(0, x / y) 
            else:
                stack.append(int(tokens.pop(0)))
        

        return stack.pop()