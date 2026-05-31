class Solution:
    def jump(self, nums: List[int]) -> int:
        current = 0
        reach = 0
        result = 0

        while reach < len(nums) - 1:
            newReach = reach
            for j in range(current, reach + 1):
                newReach = max(j + nums[j], newReach)
            current = reach
            reach = newReach
            result += 1

        return result