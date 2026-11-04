class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()

        nums2 = [nums1[0]]

        is_even = nums2[0] % 2 == 0
        #odd - even = odd, odd-odd = even, even - odd = odd, even-even = even
        seen_odd = True if not is_even else False
        for i in range(1,len(nums1)):
            if (nums1[i] % 2 == 0) == is_even:
                continue
            else:
                if seen_odd:
                    continue
                else:
                    return False


        return True


