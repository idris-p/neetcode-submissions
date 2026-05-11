class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def explore(i, path):
            if i >= len(nums):
                if sum(path) == target:
                    result.append(path.copy())
                return

            explore(i + 1, path)
            while sum(path) < target:
                path.append(nums[i])
                explore(i + 1, path)

            while path and path[-1] == nums[i]:
                path.pop()

        explore(0, [])
        return result