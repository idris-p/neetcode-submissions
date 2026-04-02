class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            pivot = nums[i]
            for j in range(0, len(nums)):
                if pivot == nums[j] and i != j:
                    return True
        return False
         