class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def validate(code):
            return 1 <= int(code) <= 26 and code[0] != "0"
        
        def dfs(index):
            if index in cache:
                return cache[index]
            if index == len(s) - 1:
                return 1 if s[index] != "0" else 0
            if index == len(s) - 2:
                if validate(s[index:]):
                    return 1 + dfs(index + 1)

            oneValid = validate(s[index])
            twoValid = validate(s[index:index + 2])

            total = 0
            if oneValid:
                total += dfs(index + 1)
            if twoValid:
                total += dfs(index + 2)

            cache[index] = total

            return total

        return dfs(0)