import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = list(Counter(nums).items())
        freq.sort(key = lambda x: x[1], reverse = True)
        
        result = []
        for digit, frequency in freq:
            result.append(digit)
            if len(result) == k:
                return result
