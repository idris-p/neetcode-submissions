class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap: Values to index
        getIndex = {}

        for i, num in enumerate(nums):
            inverse = target - num
            if inverse in getIndex:
                return [getIndex[inverse], i]
            getIndex[num] = i