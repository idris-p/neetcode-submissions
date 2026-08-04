class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[nums[0]], nums[nums[nums[0]]]

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        newSlow = nums[0]

        while slow != newSlow:
            slow, newSlow = nums[slow], nums[newSlow]

        return slow