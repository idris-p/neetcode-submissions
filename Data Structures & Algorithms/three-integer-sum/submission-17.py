class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        first = None
        result = []

        for i in range(len(nums) - 2):
            if first == nums[i]:
                continue
            first = nums[i]

            l, r = i + 1, len(nums) - 1
            while l < r:
                second = nums[l]
                third = nums[r]
                total = second + third
                if total == -first:
                    result.append([first, second, third])
                    while nums[l] == second and l < r:
                        l += 1
                    while nums[r] == third and l < r:
                        r -= 1
                elif total < -first:
                    l += 1
                elif total > -first:
                    r -= 1

        return result