class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            list1 = []
            list2 = []
            for i in range(0, len(s)):
                list1.append(s[i])
            for i in range(0, len(t)):
                list2.append(t[i])
            list1.sort()
            list2.sort()
            return (list1 == list2)

        anagrams = [[]]
        anagrams[0].append(strs[0])

        for i in range(1, len(strs)):
            added = False
            for j in range(0, len(anagrams)):
                if isAnagram(strs[i], anagrams[j][0]):
                    anagrams[j].append(strs[i])
                    added = True
            if added == False:
                anagrams.append([strs[i]])
        return anagrams