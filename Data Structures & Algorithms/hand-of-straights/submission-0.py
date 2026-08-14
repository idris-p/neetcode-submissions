import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        smallest = minHeap[0]

        while minHeap:
            start = smallest
            for i in range(groupSize):
                if start + i not in count:
                    return False
                count[start + i] -= 1

                if count[start + i] == 0:
                    pop = heapq.heappop(minHeap)
                    if pop != smallest:
                        return False
                    if minHeap:
                        smallest = minHeap[0]

        return True