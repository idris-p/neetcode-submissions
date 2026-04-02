class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        present = set()
        longest = 0

        for r in range(0, len(s)):
            while s[r] in present:
                present.remove(s[l])
                l += 1
            present.add(s[r])
            longest = max(longest, r - l + 1)

        return longest