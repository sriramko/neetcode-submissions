class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l, r, q = m - 1, m + n - 1, n - 1
        while q >= 0:
            if l >= 0 and nums1[l] > nums2[q]:
                nums1[r] = nums1[l]
                l -= 1
            else:
                nums1[r] = nums2[q]
                q -= 1
            r -= 1