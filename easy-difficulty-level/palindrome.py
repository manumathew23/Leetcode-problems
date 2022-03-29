
'''
Problem statement

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''

# Solution 1 - Converting to string

return str(x) == str(x)[::-1]

# Follow up: Could you solve it without converting the integer to a string?

# solution 1 (without string conversion)

class Solution:
  ''' Iteratively breakdown the number into digits using // (Floor division) and % (Modulus) operands, from both ends
  Compare each digit from start and end and remove the digits from the number after comparison
  Continue the comparison until the middle of number is reached or all digits are compared
  '''
    def isPalindrome(self, x: int) -> bool:
        div_factor = 1
        if x < 0:
            return False
        while abs(x // div_factor) > 9:
            div_factor *= 10

        while (abs(x) > 9):
            l = x // div_factor
            t = x % 10

            if (l != t):
                return False

            x = (x % div_factor)//10
            d = div_factor/100

        return True

'''
Above solution fails for the test case 1000021 as the number will be come 21 instead of 000021 once leading 1 is removed

'''

# Solution 2 (without string conversion)

class Solution:
  ''' Convert the integer to list of the digits
  Form the reversed number from the list
  Compare original number to the reversed number
  '''
  
    def isPalindrome(self, x: int) -> bool:
        l = []
        mul_factor = 1
        while x > 0:
            l.append(x % 10)
            mul_factor *= 10
            x //= 10

        y = 0
        while l:
            mul_factor /= 10
            y += l.pop(0) * mul_factor

        return x == y


# solution 3 (Alternative implementation of above logic)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x == 0):
            return True
        
        if(x < 0 or x % 10 == 0):
            return False
        
        temp = 0
        prev_x = x
        while (x > temp):
            pop = x % 10
            prev_x = x
            x /= 10

            temp = temp * 10 + pop;
        
        if(x == temp or prev_x == temp):
            return True
        else:
            return False
