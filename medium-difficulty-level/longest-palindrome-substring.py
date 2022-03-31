'''
Given a string s, return the longest palindromic substring in s.
 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

# solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return s[0] + s[1] if s[0] == s[1] else s[0]

        li = [(s[0], (0, 0))]
        la = fla = s[0]

        for i, v in enumerate(s[1:]):
            li.append((v, (i+1, i+1)))
            if la == v:
                li.append((la+v, (i, i+1)))
                fla = la+v
            la = v

        m = 1
        for i in li:
            ca = i[0]
            l = i[1][0]
            r = i[1][1]
            while (l <= r):
                if not (((l:=l-1) >= 0) and ((r:=r+1) < len(s))):
                    break

                if s[l] == s[r]:
                    ca = s[l] + ca + s[r]
                else:
                    break

            if len(ca) > len(fla):
                fla = ca


        return fla
