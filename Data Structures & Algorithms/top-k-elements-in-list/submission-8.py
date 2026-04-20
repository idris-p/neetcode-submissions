class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []

        for num in nums:
            seen = False
            for item in count:
                if item[0] == num:
                    item[1] += 1
                    seen = True
                    break
            if not seen:
                count.append([num, 1])

        count.sort(key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(count[i][0])

        return result
                