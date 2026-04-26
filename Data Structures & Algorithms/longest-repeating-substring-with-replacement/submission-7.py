class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        result = 0
        count = {s[r]: 1}

        while r < len(s):

            mostFrequent = 0
            for n in count.values():
                mostFrequent = max(n, mostFrequent)

            substring = s[l:r+1]
            if len(substring) - mostFrequent <= k:
                result = max(len(substring), result)
                r += 1
                if r < len(s):
                    count[s[r]] = count.get(s[r], 0) + 1
            else:
                count[s[l]] -= 1
                l += 1
        return result