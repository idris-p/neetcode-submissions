class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        if len(s) == 1:
            return s[0]


        def findLongest(centreStart, centreEnd):
            offset = 0
            longest = ""

            while 0 <= centreStart - offset and centreEnd + offset < len(s):
                if s[centreStart - offset] != s[centreEnd + offset]:
                    break
                if 2 * offset + 1 > len(longest):
                    longest = s[centreStart - offset:centreEnd + offset + 1] if centreEnd + offset + 1 < len(s) else s[centreStart - offset:]
                offset += 1

            return longest


        result = ""

        for i in range(len(s)):
            # Odd case
            odd = findLongest(i, i)
            if len(odd) > len(result):
                result = odd

            # Even case
            if i != len(s) - 1:
                even = findLongest(i, i + 1)
                if len(even) > len(result):
                    result = even

        return result