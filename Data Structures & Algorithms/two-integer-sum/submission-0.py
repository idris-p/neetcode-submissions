class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j and len(returnList) == 0:
                    returnList.append(i)
                    returnList.append(j)
                    returnList.sort()
        return returnList