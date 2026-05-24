class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robHouses(houses):
            rob1, rob2 = 0, 0

            for house in houses:
                temp = max(house + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(robHouses(nums[1:]), robHouses(nums[:-1]))