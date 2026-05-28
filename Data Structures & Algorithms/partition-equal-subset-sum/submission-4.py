class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        possibleSums = {0}

        for num in nums:
            copy = possibleSums.copy()
            for sums in possibleSums:
                new = sums + num
                if new == target:
                    return True
                copy.add(new)
            possibleSums = copy

        return False