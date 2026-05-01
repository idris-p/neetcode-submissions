class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    print(i)
                    print(stack)
                    smallerTemp, smallerIndex = stack.pop()
                    result[smallerIndex] = i - smallerIndex
            stack.append((temp, i))

        return result