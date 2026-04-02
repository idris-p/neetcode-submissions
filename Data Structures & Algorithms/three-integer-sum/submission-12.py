class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            desired = -1 * num
            while l < r:
                if nums[l] + nums[r] < desired:
                    l += 1
                elif nums[l] + nums[r] > desired:
                    r -= 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result