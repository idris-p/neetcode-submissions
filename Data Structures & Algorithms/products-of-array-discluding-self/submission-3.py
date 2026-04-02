class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        productNoZero = 1
        zeroes = 0
        for num in nums:
            product *= num
            if num != 0:
                productNoZero *= num
            else:
                zeroes += 1
        
        if zeroes > 1:
            return [0] * len(nums)

        returnList = []
        for num in nums:
            if num != 0:
                returnList.append(product // num)
            else:
                returnList.append(productNoZero)

        return returnList

        