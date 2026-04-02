class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, word in enumerate(strs):
            letters = ''.join(sorted(word))
            if letters not in anagrams:
                anagrams[letters] = [word]
            else:
                anagrams[letters].append(word)

        print(anagrams.values())
        return anagrams.values()