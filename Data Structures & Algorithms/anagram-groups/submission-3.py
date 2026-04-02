class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # letters: list of words

        for word in strs:
            if tuple(sorted(word)) in anagrams:
                anagrams[tuple(sorted(word))].append(word)
            else:
                anagrams[tuple(sorted(word))] = [word]

        return anagrams.values()