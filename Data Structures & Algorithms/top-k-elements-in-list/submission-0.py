class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def occurrences(n, array):
            count = 0
            for i in range(0, len(array)):
                if array[i] == n:
                    count += 1
            return count

        numbers = []
        for i in range(0, len(nums)):
            present = False
            for row in numbers:
                if row[0] == nums[i]:
                    present = True
            if not present:
                numbers.append([nums[i], occurrences(nums[i], nums)])

        numbers.sort(key = lambda row: row[1], reverse = True)

        returnList = []
        for i in range(0, k):
            returnList.append(numbers[i][0])

        return returnList