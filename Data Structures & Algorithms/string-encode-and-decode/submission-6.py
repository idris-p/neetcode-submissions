class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result = result + str(len(string)) + "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        l, r = 0, 1
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])
                l = r - 1
                if r + length + 1 < len(s):
                    result.append(s[l + 2:r + length + 1])
                else:
                    result.append(s[l + 2:])
                l = l + length + 2
                r = r + length + 2
            else:
                r += 1

        return result