class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq, tFreq = [0] * 26, [0] * 26

        for char in s:
            sFreq[ord(char) - ord("a")] += 1
        for char in t:
            tFreq[ord(char) - ord("a")] += 1

        return sFreq == tFreq