from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, 1
        result = []

        while l != len(nums)-1:
            desired = -1 * (nums[l] + nums[r])
            numsCopy = nums.copy()
            numsCopy.remove(nums[l])
            numsCopy.remove(nums[r])
            if desired in numsCopy:
                triplet = sorted([nums[l], nums[r], desired])
                if triplet not in result:
                    result.append(triplet)
            r += 1
            if r == len(nums):
                l += 1
                r = l + 1

        return result
                