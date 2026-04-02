class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present = set()

        for num in nums:
            if num in present:
                return True
            else:
                present.add(num)
        return False