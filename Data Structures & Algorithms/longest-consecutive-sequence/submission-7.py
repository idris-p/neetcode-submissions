class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        pointer = 0

        while pointer < len(nums):
            if not nums[pointer] - 1 in nums:
                current = 1
                while nums[pointer] + current in nums:
                    current += 1
                longest = max(current, longest)
            pointer += 1

        return longest