"""

Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

# solution 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0, nums.pop())
            k = k - 1

# Solution 2

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if k == 0 or len(nums) <= 1:
            return nums
            
        nums.reverse()
        
        if k > len(nums):
            while k > len(nums):
                k -= len(nums)
        
        def reverse(left, right, nums):
            while (left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        
        nums = reverse(k, len(nums)-1, nums)
        nums = reverse(0, k-1, nums)
        return nums

""" The following 2 solution works perfectly fine in local interpreter
but unfortunately it gives wrong output in Leetcode
"""

# Solution 3


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums = [nums.pop()] + nums
            k = k - 1

# Solution 4

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k > l:
            k = l - k
        print(nums[l-k: l] + nums[0:l-k])
