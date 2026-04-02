class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            target = -1 * num
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if not [num, nums[l], nums[r]] in result:
                        result.append([num, nums[l], nums[r]])
                    l += 1
        return result