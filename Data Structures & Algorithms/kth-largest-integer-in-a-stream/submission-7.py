import heapq, math

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)

        if len(nums) > k:
            for i in range(k, len(nums)):
                heapq.heappop(self.nums)
        elif len(nums) < k:
            for i in range(len(nums), k):
                heapq.heappush(self.nums, -math.inf)
    def add(self, val: int) -> int:
        print(self.nums)
        if not self.nums:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)

        print(self.nums)

        return self.nums[0]
