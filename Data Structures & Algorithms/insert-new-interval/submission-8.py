class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        newStart, newEnd = newInterval
        result = []

        if newEnd < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if intervals[-1][1] < newStart:
            intervals.append(newInterval)
            return intervals

        inserted = False
        for start, end in intervals:
            if inserted:
                result.append([start, end])
            else:
                if end < newStart:
                    result.append([start, end])
                elif newEnd < start:
                    result.append([newStart, newEnd])
                    result.append([start, end])
                    inserted = True
                else:
                    newStart = min(newStart, start)
                    newEnd = max(newEnd, end)
        
        if not inserted:
            result.append([newStart, newEnd])

        return result