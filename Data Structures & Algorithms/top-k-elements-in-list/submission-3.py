import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = list(Counter(nums).items())
        occurrences.sort(key = lambda x: x[1], reverse = True)
        
        returnList = []
        for num, freq in occurrences:
            returnList.append(num)
            k -= 1
            if k == 0:
                break

        return returnList