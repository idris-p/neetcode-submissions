class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1

            if str(count) in groups:
                groups[str(count)].append(string)
            else:
                groups[str(count)] = [string]

        return list(groups.values())