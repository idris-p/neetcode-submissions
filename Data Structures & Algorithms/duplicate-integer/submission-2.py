from collections import *

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for frequency in freq.values():
            if frequency > 1:
                return True
        return False