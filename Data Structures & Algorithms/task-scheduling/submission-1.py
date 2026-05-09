class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        priorityQueue = [list(x) + [-n-1] for x in count.items()]
        priorityQueue.sort(key=lambda x: x[1])

        cycle = 0
        while priorityQueue:
            i = -1
            while i >= -len(priorityQueue):
                if cycle - priorityQueue[i][2] > n:
                    priorityQueue[i][2] = cycle
                    priorityQueue[i][1] -= 1

                    if priorityQueue[i][1] == 0:
                        priorityQueue.pop(i) # :(
                    else:
                        curr = i
                        while curr - 1 >= -len(priorityQueue) and priorityQueue[curr][1] < priorityQueue[curr - 1][1]:
                            priorityQueue[curr], priorityQueue[curr - 1] = priorityQueue[curr - 1], priorityQueue[curr]
                            curr -= 1
                    break
                else:
                    i -= 1
            cycle += 1

        return cycle
            