class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        if not height:
            return 0

        i = 0
        j = len(height) - 1

        maxL = height[i]
        maxR = height[j]

        while i < j:
            if maxL < maxR:
                i += 1
                maxL = max(maxL, height[i])
                total += maxL - height[i]
            else:
                j -= 1
                maxR = max(maxR, height[j])
                total += maxR - height[j]

        return total
                

                



        
            
                


        