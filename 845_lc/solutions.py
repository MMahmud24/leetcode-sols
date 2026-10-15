class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        
        def findLength(i):
            left, right = i, i
            while left-1 >= 0 and arr[left-1] < arr[left]:
                left -= 1
            while right+1 < len(arr) and arr[right+1] < arr[right]:
                right += 1

            return (right - left + 1)

        max_len = 0
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                max_len = max(max_len, findLength(i))

        return max_len

