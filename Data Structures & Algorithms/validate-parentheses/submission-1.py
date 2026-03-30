class Solution:
    def isValid(self, s: str) -> bool:
        cor = {"]": "[", ")": "(", "}": "{"}
        stack = []

        for i in s:
            if i in cor:
                if stack and stack[-1] == cor[i]:
                    stack.pop()
                else:    
                    return False

            else:
                stack.append(i)
        
        return len(stack) == 0
        