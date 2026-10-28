class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_val = 0
        n = len(nums)

        if n == 1:
            return nums[0]

        l = 0
        r = n - 1

        while l <= r:
            if l == r:
                concat_val += nums[l]
            else:
                left = str(nums[l])
                right = str(nums[r])
                concat = left + right
                concat_val += int(concat)
            l+=1
            r-=1

        
        return concat_val



    
