class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()

        def count(target):
            l = 0
            r = len(nums)-1
            count = 0

            while l < r:
                if nums[l] + nums[r] <= target:
                    count+=r-l
                    l+=1
                else:
                    r-=1

            return count

        
        return count(upper) - count(lower-1)

'''
0 1 4 4 5 7
'''
