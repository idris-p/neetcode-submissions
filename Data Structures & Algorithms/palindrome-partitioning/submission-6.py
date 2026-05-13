class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            l, r = 0, len(string) - 1

            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

            return True

        result = []

        def explore(start, end, path):
            # if end != len(s):
            #     print("Exploring:", s[start:end])
            # else:
            #     print("Exploring:", s[start:])
            # print(start, end)
            # print(path)
            # print()
            if end == len(s):
                substring = s[start:]
                if isPalindrome(substring):
                    path.append(substring)
                    result.append(path.copy())
                    path.pop()
                return

            substring = s[start:end]
            if not isPalindrome(substring):
                return

            if substring != "":
                path.append(substring)
            i = 1
            while end + i <= len(s):
                explore(end, end + i, path)
                i += 1
            if path:
                path.pop()
            
        explore(0, 0, [])
        return result