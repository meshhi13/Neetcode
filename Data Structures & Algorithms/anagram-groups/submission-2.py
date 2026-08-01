class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {str(sorted(word)): [] for word in strs}

        for word in strs:
            copy = str(sorted(word))
            anagrams[copy].append(word)

        return list(anagrams.values())

        

