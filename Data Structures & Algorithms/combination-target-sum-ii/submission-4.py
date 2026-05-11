class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def explore(i, path, total):
            if i >= len(candidates):
                if total == target:
                    result.append(path.copy())
                return
            if total > target:
                return

            path.append(candidates[i])
            total += candidates[i]
            explore(i + 1, path, total)

            path.pop()
            total -= candidates[i]
            
            current = candidates[i]
            increment = 0
            while candidates[i + increment] == current:
                increment += 1
                if i + increment >= len(candidates):
                    break

            explore(i + increment, path, total)

        explore(0, [], 0)
        return result