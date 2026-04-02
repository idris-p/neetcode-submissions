class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = [0] * 26

        for char in s:
            occurrences[ord(char)-ord("a")] += 1

        for char in t:
            occurrences[ord(char)-ord("a")] -= 1

        return occurrences == [0] * 26