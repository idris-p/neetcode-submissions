class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        noLast = self.subsets(nums[:-1])
        withLast = [x + [nums[-1]] for x in noLast]

        return noLast + withLast