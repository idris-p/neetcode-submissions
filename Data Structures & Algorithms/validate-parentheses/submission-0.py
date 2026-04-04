class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for brace in s:
            if brace in pairs.values():
                stack.append(brace)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[brace]:
                    return False

        if stack:
            return False

        return True