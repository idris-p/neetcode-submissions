class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        pointer = 0
        while pointer < len(nums)-1:
            if nums[pointer] == nums[pointer+1]:
                nums.remove(nums[pointer])
            else:
                pointer += 1
        
        if len(nums) == 0:
            return 0
            
        currentCount = highestCount = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                currentCount += 1
            else:
                currentCount = 1
            if currentCount > highestCount:
                    highestCount = currentCount
        return highestCount
        