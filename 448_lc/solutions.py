class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        arr = [0] * (len(nums)+1)

        for num in nums:
            arr[num] = num

        res = []

        for i in range(1,len(arr)):
            if arr[i] == 0:
                res.append(i)

        return res
