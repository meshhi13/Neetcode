class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[len(stack) - 1]] < temperatures[i]:
                index = stack.pop()
                output[index] = i - index
            
            stack.append(i)
            
        return output