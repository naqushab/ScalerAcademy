## Arrays Questions Easy to Medium

1. https://leetcode.com/problems/product-of-array-except-self/

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod, suffix_prod = [1]*n, [1]*n
        for i in range(n):
            s = n-i-1
            if i == 0:
                prefix_prod[i] = nums[i]
                suffix_prod[s] = nums[s]
            else:
                prefix_prod[i] = prefix_prod[i-1] * nums[i]
                suffix_prod[s] = suffix_prod[s+1] * nums[s]
        ans = [1]*n
        for i in range(n):
            if i == 0:
                ans[i] = suffix_prod[i+1]
            elif i == n-1:
                ans[i] = prefix_prod[i-1]
            else:
                ans[i] = prefix_prod[i-1] * suffix_prod[i+1]
        return ans
```

2. https://leetcode.com/problems/backspace-string-compare/
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = collections.deque(), collections.deque()
        for ch in s:
            if ch == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        for ch in t:
            if ch == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)
        return stack1 == stack2
```

3. https://www.geeksforgeeks.org/check-if-any-two-intervals-overlap-among-a-given-set-of-intervals/  
Or  
https://leetcode.com/problems/merge-intervals/
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        temp_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > temp_interval[1]:
                merged_intervals.append(temp_interval)
                temp_interval = interval
            else:
                temp_interval[1] = max(temp_interval[1], interval[1])
        merged_intervals.append(temp_interval)
        return merged_intervals
```

4. https://www.geeksforgeeks.org/elements-that-occurred-only-once-in-the-array/
```python
import collections

def occur_once(nums):
    counter = collections.Counter(nums)
    return [k for k,v in counter.items() if v == 1]
```

5. Find the closest pair from two sorted arrays. Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.  
We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.  
Example: 
```
Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
```

6. Program to check if three points are collinear.  
Given three points, check whether they lie on a straight (collinear) or not.  
Examples : 
```
Input : (1, 1), (1, 4), (1, 5)
Output : Yes 
The points lie on a straight line

Input : (1, 5), (2, 5), (4, 6)
Output : No 
The points do not lie on a straight line
```

7. https://leetcode.com/problems/reverse-integer/  
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.  
