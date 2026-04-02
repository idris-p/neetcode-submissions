from collections import *

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurrences = Counter(nums)
        for freq in occurrences.values():
            if freq != 1:
                return True
        return False