class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def explore(parenthesis, opensUsed, balance):
            if len(parenthesis) == 2 * n:
                result.append(parenthesis)
                return

            if balance > 0:
                explore(parenthesis + ")", opensUsed, balance - 1)
            if opensUsed < n:
                explore(parenthesis + "(", opensUsed + 1, balance + 1)

        explore("(", 1, 1)
        return result