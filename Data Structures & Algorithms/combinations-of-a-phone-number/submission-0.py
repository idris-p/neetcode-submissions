class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []

        if not digits:
            return result

        def explore(i, letters):
            if len(letters) == len(digits):
                result.append(letters)
                return
            
            for letter in mapping[digits[i]]:
                explore(i + 1, letters + letter)

        explore(0, "")
        return result