class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(index):
            if index in cache:
                return cache[index]

            if index == len(s):
                return True

            possible = False
            for word in wordDict:
                if word == s[index:index + len(word)]:
                    possible = possible or dfs(index + len(word))
                    if possible:
                        return True

            cache[index] = False

            return False

        return dfs(0)