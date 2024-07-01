---
title: "Mastering LeetCode: Generating All Permutations of an Array"
seoTitle: "Solving LeetCode Permutations with Python Backtracking"
seoDescription: "Learn how to solve the "Permutations" problem on LeetCode using a backtracking approach. Follow our step-by-step guide in Python."
datePublished: Mon Jul 01 2024 15:29:17 GMT+0000 (Coordinated Universal Time)
cuid: cly34y6n5000f0ajofunoe681
slug: mastering-leetcode-generating-all-permutations-of-an-array
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1719847285146/b9ceccfc-15ab-415e-bdbc-6da9b861155f.webp
tags: interview, algorithms, python, recursion, leetcode

---

## Introduction

[Generating permutations](https://leetcode.com/problems/permutations/description/) is a fundamental problem in computer science, often appearing in coding interviews and algorithm challenges. Understanding how to efficiently generate permutations can provide insights into various combinatorial problems and improve your problem-solving skills.

In this article, we'll explore the "Permutations" problem on LeetCode and solve it using a backtracking approach.

### LeetCode Problem Statement:

> Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.
> 
> **Example 1:**
> 
> ```plaintext
> Input: nums = [1,2,3]
> Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: nums = [0,1]
> Output: [[0,1],[1,0]]
> ```
> 
> **Example 3:**
> 
> ```plaintext
> Input: nums = [1]
> Output: [[1]] 
> ```
> 
> **Constraints:**
> 
> * `1 <= nums.length <= 6`
>     
> * `-10 <= nums[i] <= 10`
>     
> * All the integers of `nums` are **unique**.
>     

## Understanding Permutations

Permutations refer to all possible arrangements of a set of elements. For an array of `n` distinct elements, there are `n!` (n factorial) possible permutations. Generating these permutations is useful in various applications, including solving puzzles, optimizing routes, and more.

## Solution Approach

To solve the permutations problem, we'll use a backtracking approach. [Backtracking](https://en.wikipedia.org/wiki/Backtracking) is an algorithmic technique for solving recursive problems by trying to build a solution incrementally and removing solutions that fail to satisfy the problem constraints.

## Detailed Solution Breakdown

### Step 1: Function Definition

We'll start by defining the main function `permute` that will take the list of integers `nums` as input and return a list of lists containing all possible permutations.

### Step 2: Helper Function

We'll define a helper function `backtrack` that will be used to generate permutations by swapping elements. This function will take the current position `start` as an argument.

### Step 3: Swapping Elements

In the `backtrack` function, we'll loop through the elements starting from the `start` index to the end of the list. For each index `i`, we'll swap the elements at indices `start` and `i`, recursively call `backtrack` with the next position `start + 1`, and then swap the elements back to their original positions.

### Code Implementation

Here's the complete Python code for generating permutations:

```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(start: int):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # swap back

    result = []
    backtrack(0)
    return result

# Test cases
print(permute([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0, 1]))    # Output: [[0,1],[1,0]]
print(permute([1]))       # Output: [[1]]
```

### Explanation of the Code

1. **Function Definition**:
    
    * The `permute` function takes a list `nums` and returns a list of lists containing all permutations.
        
2. **Backtracking Function**:
    
    * We define a nested function `backtrack` that takes the current position `start` as an argument.
        
    * If `start` equals the length of `nums`, we've reached a complete permutation, so we append a copy of `nums` to the `result` list.
        
3. **Swapping Elements**:
    
    * We loop through the elements starting from the `start` index.
        
    * For each index `i`, we swap the elements at indices `start` and `i`.
        
    * We recursively call `backtrack` with `start + 1`.
        
    * After the recursive call, we swap the elements back to their original positions.
        
4. **Result Storage**:
    
    * We initialize an empty list `result` to store all permutations.
        
    * We call `backtrack` starting from index 0.
        
    * Finally, we return the `result` list containing all permutations.
        

![hart showing the recursive calls and swaps.  Alt Text: "Flowchart of recursive calls and element swaps in the backtracking algorithm.](https://cdn.hashnode.com/res/hashnode/image/upload/v1719847629932/4ea1b1a3-4fbf-44a5-8717-c9ad0306b077.png align="center")

## Time Complexity Analysis

The time complexity of this solution is O(n \* n!), where `n` is the length of the input list. This is because there are `n!` permutations, and we need to copy each permutation of length `n` to the result list. Given the constraint (1 &lt;= nums.length &lt;= 6), this complexity is acceptable.

## Common Questions and Pitfalls

### Q1: What is the maximum length of the input list?

* A1: The length of the input list is between 1 and 6.
    

### Q2: Are duplicate elements allowed in the input list?

* A2: No, all integers in the input list are unique.
    

### Q3: Why use backtracking for this problem?

* A3: Backtracking efficiently explores all possible permutations by making choices and undoing them when necessary.
    

## FAQ Section

### What is the maximum length of the input list?

The input list can have a length between 1 and 6.

### Are duplicate elements allowed in the input list?

No, all integers in the input list must be unique.

### Why use backtracking for this problem?

Backtracking is efficient for generating all permutations by making choices and backtracking to previous states when necessary.

## Conclusion

Generating permutations is a classic problem that can be efficiently solved using a backtracking approach. By understanding and implementing the solution step-by-step, you can enhance your problem-solving skills and tackle similar combinatorial problems with confidence.

Practice more permutation problems to deepen your understanding and improve your coding abilities.

### Related Articles

* "[Conquer the Binary Search: Mastering LeetCode’s Rotated Sorted Array Challenge](https://blog.seancoughlin.me/conquer-the-binary-search-mastering-leetcodes-rotated-sorted-array-challenge)"
    
* "[Solving LeetCode's Combination Sum Problem: Optimized Techniques for Efficient Solutions](https://blog.seancoughlin.me/solving-leetcodes-combination-sum-problem-optimized-techniques-for-efficient-solutions)"
    
* "[Getting Started with Studying for Software Engineering Interviews Using LeetCode](https://blog.seancoughlin.me/getting-started-with-studying-for-software-engineering-interviews-using-leetcode)"