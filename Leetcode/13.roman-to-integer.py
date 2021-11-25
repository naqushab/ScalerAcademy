#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (57.67%)
# Likes:    2289
# Dislikes: 163
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given a roman numeral, convert it to an integer.
# 
# 
# Example 1:
# 
# 
# Input: s = "III"
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: s = "IV"
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: s = "IX"
# Output: 9
# 
# 
# Example 4:
# 
# 
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
# 
# 
#

# @lc code=start
class Solution:
    def get_digit_from_roman_char(self, str_num: str) -> int:
        if str_num == 'I':
            num = 1
        elif str_num == 'V':
            num = 5
        elif str_num == 'X':
            num = 10
        elif str_num == 'L':
            num = 50
        elif str_num == 'C':
            num = 100
        elif str_num == 'D':
            num = 500
        elif str_num == 'M':
            num = 1000
        return num

    def romanToInt(self, s: str) -> int:
        ans = self.get_digit_from_roman_char(s[-1])
        for i in range(len(s)-2, -1, -1):
            num_a = self.get_digit_from_roman_char(str_num=s[i+1])
            num_b = self.get_digit_from_roman_char(str_num=s[i])
            if num_b < num_a:
                ans -= num_b
            else:
                ans += num_b
        return ans
            
            
            
# @lc code=end

