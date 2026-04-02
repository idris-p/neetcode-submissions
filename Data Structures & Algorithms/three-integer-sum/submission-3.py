class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sumToZero = []

        for i in range(0, len(nums)-2):
            for j in range(1+i, len(nums)-1):
                for k in range(1+j, len(nums)):
                    print(i, j, k)
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in sumToZero:
                            sumToZero.append(triplet)

        return sumToZero