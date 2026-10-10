# This is the two pointer approach with constant space

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        l1, l2 = 0,0
        i = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                nums1[i] = nums1[l1]
                l1 += 1
                l2 += 1
                i += 1
            elif nums1[l1] < nums2[l2]:
                while l1 < len(nums1) and nums1[l1] < nums2[l2]:
                    l1+=1
            else:
                while l2 < len(nums2) and nums2[l2] < nums1[l1]:
                    l2+=1
        if i == 0:
            return []
        k = 1
        for j in range(1,i):
            if nums1[j] != nums1[j-1]:
                nums1[k] = nums1[j]
                k+=1

        return nums1[:k]
