class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hashMap:
                return [hashMap[compliment], i]
            hashMap[num] = i