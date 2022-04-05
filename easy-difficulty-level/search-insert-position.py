''' PROBLEM STATEMENT

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

'''

''' TEST CASES
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7
[1]
0
[1,3,5,6]
0
'''

# Solution 1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        l = len(nums)
        e = l
        while s <= e:
            m = s + (e-s)//2
            n = nums[m]
            if target == n or (nums[m-1] < target and n > target):
                return m
            elif n < target:
                if m + 1 == l or nums[m+1] > target:
                    return m + 1
                s = m + 1
            else:
                e = m - 1
        return 0

# Solution 2 (using Python inbuilt function bisect_left)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
