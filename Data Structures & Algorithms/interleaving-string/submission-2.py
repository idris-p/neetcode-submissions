class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = set()
        
        def dfs(p1, p2):
            if p1 + p2 >= len(s3):
                return True
            if (p1, p2) in cache:
                return False

            found = False

            if p1 < len(s1) and s1[p1] == s3[p1 + p2]:
                found = found or dfs(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p1 + p2]:
                found = found or dfs(p1, p2 + 1)

            cache.add((p1, p2))

            return found

        return dfs(0, 0)