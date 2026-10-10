class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        seen = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            seen[nums[i]].append(i)

        for arr in seen.values():
            if len(arr) != 3:
                continue
            
            if arr[1] - arr[0] == arr[2] - arr[1]:
                count+=1

        return count

