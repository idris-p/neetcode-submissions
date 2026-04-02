import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "").lower()

        if len(s) == 0:
            return True
            
        half = len(s) // 2
        for i in range(0, half + 1):
            if s[i] != s[len(s)-1-i]:
                return False
        return True