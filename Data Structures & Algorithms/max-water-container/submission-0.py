class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(0, len(heights)-1):
            for j in range(1+i, len(heights)):
                if heights[i] < heights[j]:
                    area = abs(j - i) * heights[i]
                else:
                    area = abs(j - i) * heights[j]
                if area > maximum:
                    maximum = area

        return maximum
        