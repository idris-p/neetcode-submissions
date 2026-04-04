import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = [-num for num in nums]
        heapq.heapify(self.maxHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)

        copy = self.maxHeap.copy()

        for i in range(0, self.k - 1):
            heapq.heappop(self.maxHeap)

        print(self.maxHeap)

        result = -1 * self.maxHeap[0]

        self.maxHeap = copy

        return result