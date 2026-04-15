class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        eatingRate = 0
        while j != i:
            eatingRate = (i + j) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / eatingRate)


            if hours > h:
                i = eatingRate + 1
            else:
                j = eatingRate

        return j