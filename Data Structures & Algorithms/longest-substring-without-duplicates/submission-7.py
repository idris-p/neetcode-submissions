class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def hasDuplicate(string):
            present = []
            for i in range(0, len(string)):
                if string[i] not in present:
                    present.append(string[i])
                else:
                    return True
            return False

        if len(s) == 0:
            return 0
        maximum = 1
        
        for start in range(0, len(s)):
            for end in range(start, len(s)):
                if not hasDuplicate(s[start:end]):
                    maximum = max(len(s[start:end]), maximum)
            if not hasDuplicate(s[start:]):
                maximum = max(len(s[start:]), maximum)

        return maximum

        