class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {n: [] for n in range(numCourses)}

        for a, b in prerequisites:
            preMap[a].append(b)

        visited = set()
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)

            if not preMap[course]:
                visited.remove(course)
                return True

            result = True
            for pre in preMap[course]:
                result = result and dfs(pre)
                if not result:
                    return False

            visited.remove(course)
            return True

        
        for course in preMap:
            if preMap[course]:
                result = dfs(course)
                if not result:
                    return False

        return True