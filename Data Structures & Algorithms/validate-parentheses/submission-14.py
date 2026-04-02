class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for brace in s:
            if brace == "(" or brace == "{" or brace == "[":
                stack.append(brace)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if pairs[brace] != popped:
                    return False
        
        if not stack:
            return True
        else:
            return False