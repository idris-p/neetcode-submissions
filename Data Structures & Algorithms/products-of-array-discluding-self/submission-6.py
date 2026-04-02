class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        premult = 1
        for i, num in enumerate(result):
            result[i] *= premult
            premult *= nums[i]

        postmult = 1
        for i in range(len(result)-1, -1, -1):
            result[i] *= postmult
            postmult *= nums[i]

        return result    