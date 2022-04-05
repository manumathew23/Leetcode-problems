"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

"""


# TESTCASES

"""

[-4,-1,0,3,10]
[-7,-3,2,3,11]

"""

# Solution 1


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums]) # trivial approach


      
# Solution 2
""" Trivial and less efficient: Sorting at each line """

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f = []
        for item in nums:
            f.append(item**2)
            f.sort()
        return f



"""

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""

# Solution 2
"""
Using 2 pointers: one from left, one from right
Compare each pointer and inserting largest at 0th position
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        f = []
        while l <= r:
            ln = nums[l]**2
            rn = nums[r]**2
            if ln >= rn:
                f.insert(0, (ln))
                l += 1
            else:
                f.insert(0, rn)
                r -= 1
        return f


# Solution 2
"""

Using bisect_left to find the correct insert position for each element

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f = []
        for item in nums:
            item = item**2
            f.insert(bisect_left(f, item), item)
        return f
