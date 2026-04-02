import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
        
        for i in range(0, len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False

        return True
