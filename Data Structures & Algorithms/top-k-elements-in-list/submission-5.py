import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digitToFreq, freqToDigit = defaultdict(int), {}

        for i, num in enumerate(nums):
            digitToFreq[num] += 1
            freqToDigit[i+1] = []

        for digit, freq in digitToFreq.items():
            freqToDigit[freq].append(digit)

        result = []

        for i in range(len(freqToDigit), 0, -1):
            for digit in freqToDigit[i]:
                result.append(digit)
                if len(result) == k:
                    return result