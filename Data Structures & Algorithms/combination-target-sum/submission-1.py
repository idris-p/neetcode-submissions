class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def explore(i, path, total):
            if i >= len(nums):
                if total == target:
                    result.append(path.copy())
                return

            explore(i + 1, path, total)
            while total < target:
                path.append(nums[i])
                total += nums[i]
                explore(i + 1, path, total)

            while path and path[-1] == nums[i]:
                path.pop()
                total -= nums[i]

        explore(0, [], 0)
        return result