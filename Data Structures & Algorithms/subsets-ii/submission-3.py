class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def explore(i, path):
            print("i", i)
            print("path", path)
            if i == len(nums):
                result.append(path.copy())
                return

            
            path.append(nums[i])
            explore(i + 1, path)
            path.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            explore(i + 1, path)

        explore(0, [])

        return result