class Solution:
    def minWindow(self, s: str, t: str) -> str:
            input_list = dict(Counter(t))
            input_set = set(t)
            i = 0
            j = 0

            minI = 0
            minLen = math.inf

            def satisfied():
                for item in input_list.values():
                    if item > 0:
                        return False

                return True

            if len(t) > len(s):
                return ""

            while j < len(s):
                if s[j] in input_list:
                    input_list[s[j]] -= 1
                
                j += 1

                while satisfied():
                    if j - i < minLen:
                        minLen = j - i
                        minI = i
                
                    if s[i] in input_set:
                        input_list[s[i]] = input_list.get(s[i], 0) + 1

                    i += 1

            if minLen == math.inf:
                return ""
                
            return s[minI: minI + minLen]
