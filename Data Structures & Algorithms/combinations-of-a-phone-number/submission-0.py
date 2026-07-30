class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        if not digits:
            return []

        def dfs(index, current):
            if index == len(digits):
                res.append(current)
                return

            for letter in digit_map[digits[index]]:
                dfs(index + 1, current + letter)

        dfs(0, "")
        return res