class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = [0] * 26, [0] * 26

        for c in s:
            sCount[ord(c)-ord("a")] += 1
        for c in t:
            tCount[ord(c)-ord("a")] += 1

        return sCount == tCount