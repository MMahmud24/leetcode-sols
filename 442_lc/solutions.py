class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if nums[i] == i+1:
                continue

            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])

        return res
