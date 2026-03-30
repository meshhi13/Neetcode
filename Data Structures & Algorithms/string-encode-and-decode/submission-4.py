class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "~~~~~~~"
        result = ""

        for i in strs[:len(strs) - 1]:
            result += i + "/~~"

        if len(strs) > 0:
            result += strs[-1]

        return result
    def decode(self, s: str) -> List[str]:
        if s == "~~~~~~~":
            return []
        return s.split("/~~")