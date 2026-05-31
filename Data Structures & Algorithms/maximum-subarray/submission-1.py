class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        result = -math.inf

        while r < len(nums):
            if total < 0:
                total = 0
                l = r
            total += nums[r]
            r += 1

            result = max(total, result)

        return result