class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        for i in range(0, len(s)):
            list1.append(s[i])
        for i in range(0, len(t)):
            list2.append(t[i])

        list1.sort()
        list2.sort()

        return (list1 == list2)