class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Value: Index
        hashMap = {}

        for i, num in enumerate(nums):
            inverse = target - num
            if inverse in hashMap:
                return [hashMap[inverse], i]
            hashMap[num] = i