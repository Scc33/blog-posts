---
title: "How to Find First and Last Position of Element in Sorted Array"
seoTitle: "How to Find First and Last Position of Element in Sorted Array"
seoDescription: "Discover first & last positions of target in sorted array using binary search. Efficient O(log n) solution for large datasets."
datePublished: Tue Sep 05 2023 23:18:35 GMT+0000 (Coordinated Universal Time)
cuid: clm6xm5xn000309l54ujj0epw
slug: how-to-find-first-and-last-position-of-element-in-sorted-array
tags: interviews, algorithms, leetcode, binary-search, binary-search-algorithm

---

## The Problem

With this article, I will be covering the [Find First and Last Position of an Element in a Sorted Array problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/).

Leetcode describes the problem with the following:

> Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
> 
> If `target` is not found in the array, return `[-1, -1]`.
> 
> You must write an algorithm with `O(log n)` runtime complexity.

Example:

> Input: nums = \[5,7,7,8,8,10\], target = 8
> 
> Output: \[3,4\]

Leetcode ranks this problem as a medium. I think that is an appropriate rating. The solution is feasible but does require some algorithmic understanding.

### Naive Approach and Its Limitations

The naive approach for solving this problem would be to scan through the array linearly to find the first and last occurrence of the target value. This involves looping through the array once to find the first occurrence of the target and marking that index as the starting position, then looping through it again to find the last occurrence and marking that as the ending position.

While this approach works, it takes `O(n)` time to solve, which doesn't meet the constraint of `O(log n)` runtime complexity. Therefore, it would become inefficient when dealing with large datasets.

## The Solution

To achieve a runtime complexity of `O(log n)`, we can use [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm). A binary search is possible because the array is already sorted. In this optimized approach, we will perform two binary searches:

1. **Finding the Leftmost Position**: The first binary search will find the leftmost or the first occurrence of the target value.
    
2. **Finding the Rightmost Position**: The second binary search will find the rightmost or the last occurrence of the target value.
    

Here's how each binary search would work:

1. **Leftmost Position**: Initialize `left` to 0 and `right` to `n - 1` (where `n` is the length of the array). In the while loop, calculate the middle index as `(left + right) // 2`. If `target > nums[mid]`, set `left = mid + 1`. Otherwise, set `right = mid - 1`. After the loop, check if `nums[left]` is the target to confirm.
    
2. **Rightmost Position**: Initialize `left` to 0 and `right` to `n - 1` again. This time, if `target >= nums[mid]`, set `left = mid + 1`. Otherwise, set `right = mid - 1`. After the loop, check if `nums[right]` is the target to confirm.
    
3. Finally return \[-1, -1\] if the location of the left and right position overlap.
    

Notice that the key difference between the left and right searches is the use of the greater than or equal to check on the right search.

```python
class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target > nums[mid]: 
                left = mid + 1
            else: 
                right = mid - 1
        left_to_return = left
                
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target >= nums[mid]: 
                left = mid + 1
            else: 
                right = mid - 1

        if left_to_return <= right:
            return (left_to_return, right) 
        else:
            return [-1, -1]
```

### Time Complexity

Each binary search has a time complexity of `O(log n)`, and since we are performing two binary searches, the overall time complexity remains `O(log n)`.

This optimized approach not only meets the problem's algorithmic constraint but also efficiently finds the target's starting and ending positions in the array.