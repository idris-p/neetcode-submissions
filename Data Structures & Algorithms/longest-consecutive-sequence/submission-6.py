class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current = 1
                while num + current in nums:
                    current += 1
                longest = max(current, longest)

        return longest