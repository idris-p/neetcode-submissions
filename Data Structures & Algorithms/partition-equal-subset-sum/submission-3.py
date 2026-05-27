class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2


        def dfs(subset, total, start):
            nonlocal target

            if total == target:
                return True
            if len(subset) == len(nums):
                return False

            found = False
            for i in range(start, len(nums)):
                found = found or dfs(subset + [nums[i]], total + nums[i], i + 1)
                if found:
                    return True

            return False

        return dfs([], 0, 0)