class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def explore(i, path, seen):
            if i == len(nums):
                result.append(path.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in seen:
                    path.append(nums[j])
                    seen.add(nums[j])
                    explore(i + 1, path, seen)
                    path.pop()
                    seen.remove(nums[j])

        explore(0, [], set())
        return result