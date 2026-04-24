class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()

        for num in nums:
            hashSet.add(num)

        longest = 0
        for num in hashSet:
            if num - 1 not in hashSet:
                current = 1
                while num + current in hashSet:
                    current += 1
                longest = max(current, longest)

        return longest
