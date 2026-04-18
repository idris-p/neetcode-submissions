class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphanum(char: str) -> bool:
            return ((ord("a") <= ord(char) <= ord("z")) or (ord("A") <= ord(char) <= ord("Z")) or (ord("0") <= ord(char) <= ord("9")))

        l, r = 0, len(s) - 1

        while l < r:
            while not isAlphanum(s[l]) and l < r:
                l += 1
            while not isAlphanum(s[r]) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True