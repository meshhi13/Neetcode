class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            copy = str(sorted(word))
            if word in anagrams:
                continue
            anagrams[copy] = []

        for word in strs:
            copy = str(sorted(word))
            anagrams[copy].append(word)

        return list(anagrams.values())

        

