class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = []
        rightProduct = []

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            leftProduct.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            rightProduct = [product] + rightProduct

        result = []
        result.append(rightProduct[1])
        for i in range(len(nums) - 2):
            result.append(leftProduct[i] * rightProduct[i + 2])
        result.append(leftProduct[-2])

        return result