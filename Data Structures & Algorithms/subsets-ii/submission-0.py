class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def explore(i, path, ignored):
            if i == len(nums):
                result.append(path.copy())
                return

            if nums[i] not in ignored:
                path.append(nums[i])
                explore(i + 1, path, ignored)
                ignored.add(path.pop())
                explore(i + 1, path, ignored)
                ignored.remove(nums[i])
            else:
                explore(i + 1, path, ignored)

        explore(0, [], set())
        return result