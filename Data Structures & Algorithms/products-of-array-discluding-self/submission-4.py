class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        premult = 1
        for i in range(0, len(nums) - 1):
            premult *= nums[i]
            result.append(premult)

        postmult = 1
        for i in range(len(result)-1, -1, -1):
            result[i] *= postmult
            postmult *= nums[i]

        return result

        