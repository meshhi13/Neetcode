class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(current, nOpen, nClose):
            if nClose == 0:
                return ""

            if nOpen == 0:
                return current + ")" * nClose

            if nClose < nOpen:
                return ""

            output.append(backtrack(current + ")", nOpen, nClose - 1))
            output.append(backtrack(current + "(", nOpen - 1, nClose))
            return ""

        backtrack("", n, n)

        res = []

        for i in output:
            if i != "":
                res.append(i)

        return res

