class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def partition_recursive(current: List[str], new_s: str) -> List[str]:
            if not new_s:
                result.append(current.copy())
                return

            for i in range(len(new_s)):
                if new_s[:i + 1] == new_s[:i + 1][::-1]:
                    current.append(new_s[:i+1])
                    print(current)
                    partition_recursive(current, new_s[i+1:])
                    current.pop()
                    

        partition_recursive([], s)

        return result

