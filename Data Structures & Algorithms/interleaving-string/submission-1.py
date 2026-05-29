class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = [[None for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        
        def dfs(p1, p2):
            if p1 + p2 >= len(s3):
                return True
            if cache[p1][p2] != None:
                return cache[p1][p2]

            found = False

            if p1 < len(s1) and s1[p1] == s3[p1 + p2]:
                found = found or dfs(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p1 + p2]:
                found = found or dfs(p1, p2 + 1)

            cache[p1][p2] = found

            return found

        return dfs(0, 0)