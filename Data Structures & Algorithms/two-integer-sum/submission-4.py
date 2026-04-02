import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, val in enumerate(nums):
            if target - val in hashMap.keys():
                return [hashMap[target - val], i]

            hashMap[val] = i