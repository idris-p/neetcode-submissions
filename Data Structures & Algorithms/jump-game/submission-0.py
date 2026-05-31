class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump >= len(nums):
                    break
                if dp[i + jump] == True:
                    dp[i] = True
                    break

        return dp[0]