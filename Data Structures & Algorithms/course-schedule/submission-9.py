class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = {n: [] for n in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        studied = set()
        numTaken = 0
        def dfs(course):
            nonlocal numTaken

            if course in studied:
                return False
            if course in visited:
                return True

            visited.add(course)
            studied.add(course)
            numTaken += 1

            noCycle = True
            for pre in graph[course]:
                noCycle = noCycle and dfs(pre)
                if not noCycle:
                    return False

            studied.remove(course)
            return True

        for course in graph:
            if course not in visited:
                if not dfs(course):
                    return False

        return numTaken == numCourses