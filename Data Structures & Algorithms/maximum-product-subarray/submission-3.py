class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct, minProduct = 1, 1
        result = max(nums)

        for num in nums:
            temp = max(num, num * maxProduct, num * minProduct)
            minProduct = min(num, num * maxProduct, num * minProduct)
            maxProduct = temp

            result = max(maxProduct, result)

        return result