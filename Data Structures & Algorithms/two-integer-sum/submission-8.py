class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # number: index

        for i, num in enumerate(nums):
            desired = target - num
            if desired in hashMap:
                return [hashMap[desired], i]
            hashMap[num] = i