class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getLetterCount(string):
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            return count

        count = getLetterCount(s1)

        for i in range(len(s2) - len(s1) + 1):
            if i + len(s1) < len(s2):
                substring = s2[i:i + len(s1)]
            else:
                substring = s2[i:]

            if count == getLetterCount(substring):
                return True

        return False