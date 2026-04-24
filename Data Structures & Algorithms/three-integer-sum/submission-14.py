class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev = None
        
        for i in range(len(nums)):
            if prev == nums[i]:
                continue
            target = -nums[i]
            index = {}
            seen = set()
            
            for j in range(i + 1, len(nums)):
                if nums[j] in seen:
                    continue
                inverse = target - nums[j]

                if inverse in index:
                    if index[inverse] == i or index[inverse] == j:
                        continue
                    result.append([nums[i], inverse, nums[j]])
                    seen.add(nums[j])
                else:
                    index[nums[j]] = j
            prev = nums[i]

        return result
