'''

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)

'''


# Solution

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo+hi)//2
            tot, cnt = 0, 1
            for num in nums:
                if tot+num<=mid: 
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt>m: lo = mid+1
            else: hi = mid
        return hi

''' Solution explanation

The minimum value of sum cannot be lower than the largest element of the array nums . This is because even if we split all element into group of size 1, largest element will have the largest sum.

So, this value will be the staring range of Binary Search.

e.g. if nums = [7,2,5,10,8], then sum cannot be lower that 10.

Similarly, the largest possible value of Sum will be when we don't divide the array at all and all elements are in the same group.

Ending range of Binary Search will be the sum of the whole array nums.

We will then calculate mid value of this range and check if We can have atmost m subarray groups, such that the sum of each group does not exceed mid.

To do this, we can take a variable count to store the number of paritions needed so that the maximum sum of the nums does not exceed mid.

If the total number of groups after partition is less than the m, we can split the any of the current group of size >=2.
This will not increase the maximum sum and hence our answer will still be valid.
'''
