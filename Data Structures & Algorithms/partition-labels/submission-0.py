class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterToLast = {}

        for i in range(len(s)):
            letterToLast[s[i]] = i
        
        length = end = 0
        result = []

        for i in range(len(s)):
            end = max(end, letterToLast[s[i]])
            length += 1
            if i == end:
                result.append(length)
                length = 0

        return result