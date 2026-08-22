class CountSquares:

    def __init__(self):
        # Store points in hashMap by x
        self.points = {}

    def add(self, point: List[int]) -> None:
        # Add point to hashMap
        if point[0] in self.points:
            self.points[point[0]].append(point[1])
        else:
            self.points[point[0]] = [point[1]]

    def count(self, point: List[int]) -> int:
        # Loop through x in hashMap
        # For each value in x check if two points that form square exist (or mirror)
        # Increment result

        result = 0
        x1, y1 = point

        if x1 not in self.points:
            return result

        def countSquares(x, y1, y2):
            if x not in self.points:
                return 0

            y1Count, y2Count = 0, 0
            for y in self.points[x]:
                if y == y1:
                    y1Count += 1
                elif y == y2:
                    y2Count += 1
            return y1Count * y2Count

        for y2 in self.points[x1]:
            if y1 == y2:
                continue
            length = abs(y1 - y2)
            # (point0, point1) (point0, y)
            # +-length         +-length

            x = x1 + length
            result += countSquares(x, y1, y2)
            
            x = x1 - length
            result += countSquares(x, y1, y2)

        return result
