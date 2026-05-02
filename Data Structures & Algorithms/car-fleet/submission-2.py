class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for car in cars:
            stack.append(car)
            if len(stack) > 1:
                frontDestinationTime = (target - stack[-2][0]) / stack[-2][1]
                behindDestinationTime = (target - stack[-1][0]) / stack[-1][1]

                if behindDestinationTime <= frontDestinationTime:
                    stack.pop()

        return len(stack)