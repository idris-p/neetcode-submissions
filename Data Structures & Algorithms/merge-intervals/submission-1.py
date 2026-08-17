class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        result = []
        i = 0

        while i < len(intervals):
            new = intervals[i]
            while i < len(intervals) - 1 and new[1] >= intervals[i + 1][0]:
                new[1] = max(new[1], intervals[i + 1][1])
                i += 1
            result.append(new)
            i += 1

        return result