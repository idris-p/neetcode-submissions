class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {} # number: frequency

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            if freq[num] > 1:
                return True

        return False