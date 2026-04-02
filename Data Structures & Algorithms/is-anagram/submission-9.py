class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurences = [0] * 26

        for i in range(0, len(s)):
            occurences[ord(s[i])-ord("a")] += 1
            occurences[ord(t[i])-ord("a")] -= 1

        if occurences == [0] * 26:
            return True
        else:
            return False

        