class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {n: [] for n in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        path = set()
        result = []
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            visited.add(course)
            path.add(course)

            for pre in graph[course]:
                noCycle = dfs(pre)
                if not noCycle:
                    return False

            result.append(course)

            path.remove(course)
            return True

        for course in graph:
            if course not in visited:
                noCycle = dfs(course)
                if not noCycle:
                    return []
        
        return result