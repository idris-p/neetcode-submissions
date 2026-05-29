class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [{} for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for total, count in dp[i - 1].items():
                dp[i][total - nums[i - 1]] = count + dp[i].get(total - nums[i - 1], 0)
                dp[i][total + nums[i - 1]] = count + dp[i].get(total + nums[i - 1], 0)

        if target in dp[len(nums)]:
            return dp[len(nums)][target]
        else:
            return 0