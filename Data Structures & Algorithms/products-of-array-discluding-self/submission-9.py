class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        product = 1

        for i in range(len(nums)-1):
            product *= nums[i]
            result.append(product)

        product = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result