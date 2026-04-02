import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digitToFreq = {}
        freqToDigit = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            digitToFreq[num] = 1 + digitToFreq.get(num, 0)

        for digit, freq in digitToFreq.items():
            freqToDigit[freq].append(digit)

        for i in range(len(nums), 0, -1):
            for digit in freqToDigit[i]:
                result.append(digit)
                if len(result) == k:
                    return result