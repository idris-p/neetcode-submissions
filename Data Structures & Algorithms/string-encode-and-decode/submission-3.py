class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l, r = 0, 0
        while r < len(s):
            r += 1
            if s[r] == "#":
                length = int(s[l:r])
                decoded.append(s[r+1:r+1+length])
                l, r = r + 1 + length, r + 1 + length

        return decoded
