class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = [0] * 26, [0] * 26

        for char in s:
            sCount[ord(char)-ord("a")] += 1
        for char in t:
            tCount[ord(char)-ord("a")] += 1

        return sCount == tCount