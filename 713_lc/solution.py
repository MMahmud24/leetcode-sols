class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        count = 0
        l = 0
        curr = 1
        for r, num in enumerate(nums):
            curr = curr * num

            while l <= r and curr >= k:
                curr = curr // nums[l]
                l+=1

            count += r - l + 1

        return count
