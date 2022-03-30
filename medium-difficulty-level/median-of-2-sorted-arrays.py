'''

4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''

# Solution 1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        f = []
        l1 = len(nums1)
        l2 = len(nums2)

        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                f.append(nums1[i])
                i += 1
            else:
                f.append(nums2[j])
                j += 1

        if i < l1:
            f += (nums1[i:])
        elif j < l2:
            f += (nums2[j:])

        m = (l1 + l2)
        if m%2 == 0:
            return (f[(m//2)-1] + f[(m//2)])/2
        else:
            return f[m//2]


# solution 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f = sorted(nums1 + nums2)
        m = len(f)
        if m%2 == 0:
            return (f[(m//2)-1] + f[(m//2)])/2
        else:
            return f[m//2]
