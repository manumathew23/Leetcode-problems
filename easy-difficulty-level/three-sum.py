''' Problem statement

This is another article in the series leetcode problem solutions and this article is a solution to leetcode 15 three sum problem.


We solved the two sum problem in our earlier article, and this problem in some ways is a continuation of the two sum problem. So, if you have not yet solved the two sum problem we advice you to do so because it will help you understand the 3 sum problem better.


Given an array of integers, nums, return all the triplets in the given array nums[i], nums[j], nums[k] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


Notice: The solution set must not contain duplicate triplets.


Example

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = [0]
Output: []


'''

# Solution logic

'''

1. Sort the list in descending order (ascending order is also fine, but below logic need to be reversed accordingly)
2. Create two pointers - One from start of the sorted list, one from end of it
3. Add the values at both pointers and then move start pointer by one position and add it's value to the sum
4. If the value is greater than the expected result in question, move the end pointer one position towards left to calculate next sum.
5. If the value is lesser than the expected result in question, move the start pointer one position towards right to calculate next sum.

'''

# Solution code

class Solution(object):

    def threeSum(self, nums):

        # Sort the given array

        nums.sort()

        result = []
        for num1Idx in xrange(len(nums) - 2):

            # Skip all duplicates from left
            # num1Idx>0 ensures this check is made only from 2nd element onwards

            if num1Idx > 0 and nums[num1Idx] == nums[num1Idx - 1]:
                continue
            (num2Idx, num3Idx) = (num1Idx + 1, len(nums) - 1)

            while num2Idx < num3Idx:
                sum = nums[num1Idx] + nums[num2Idx] + nums[num3Idx]

                if sum == 0:

                    # Add triplet to result

                    result.append((nums[num1Idx], nums[num2Idx],
                                  nums[num3Idx]))

                    num3Idx -= 1

                    # Skip all duplicates from right

                    while num2Idx < num3Idx and nums[num3Idx] \
                        == nums[num3Idx + 1]:
                        num3Idx -= 1
                elif sum > 0:

                    # Decrement num3Idx to reduce sum value

                    num3Idx -= 1
                else:

                    # Increment num2Idx to increase sum value

                    num2Idx += 1
        return result
