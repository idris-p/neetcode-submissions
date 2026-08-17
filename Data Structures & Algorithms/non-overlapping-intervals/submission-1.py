class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        
        endVal = intervals[0][1]
        result = 0

        for i in range(1, len(intervals)):
            if endVal > intervals[i][0]:
                result += 1
                endVal = min(endVal, intervals[i][1])
            else:
                endVal = intervals[i][1]

        return result