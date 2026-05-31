class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump >= len(nums):
                    break
                dp[i] = min(1 + dp[i + jump], dp[i])

        return dp[0]