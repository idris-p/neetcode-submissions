class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            l, r = 0, len(self.timeMap[key]) - 1

            while l <= r:
                m = l + (r - l) // 2

                if self.timeMap[key][m][0] == timestamp:
                    self.timeMap[key][m][1] = value
                    break
                elif self.timeMap[key][m][0] > timestamp:
                    r = m - 1
                elif self.timeMap[key][m][0] < timestamp:
                    l = m + 1

            self.timeMap[key].insert(m + 1, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ""

        l, r = 0, len(self.timeMap[key]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if self.timeMap[key][m][0] == timestamp:
                return self.timeMap[key][m][1]
            elif self.timeMap[key][m][0] > timestamp:
                r = m - 1
            elif self.timeMap[key][m][0] < timestamp:
                l = m + 1

        if self.timeMap[key][m][0] < timestamp:
            return self.timeMap[key][m][1]
        else:
            return self.timeMap[key][m - 1][1]