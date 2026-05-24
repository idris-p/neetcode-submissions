class Solution:
    def rob(self, nums: List[int]) -> int:
        
        table = [0] * len(nums)

        pointer = 0

        while pointer < len(table):
            if pointer == 0:
                table[0] = nums[0]
            elif pointer == 1:
                table[1] = max(table[0], nums[1])
            else:
                table[pointer] = max(table[pointer - 1], table[pointer - 2] + nums[pointer])
            pointer += 1

        return table[-1]