class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        if len(s) == 0 or len(s) == 1:
            return len(s)

        l, r = 0, 1
        seen = set(s[l])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(r - l + 1, longest)
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return longest