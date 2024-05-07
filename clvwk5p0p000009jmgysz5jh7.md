---
title: "Mastering the Challenge: Solve 'Longest Substring Without Repeating Characters' on LeetCode"
seoTitle: "LeetCode Guide: Longest Substring Without Repeats"
seoDescription: "Master the 'Longest Substring Without Repeating Characters' on LeetCode with our detailed guide and Python solution."
datePublished: Tue May 07 2024 15:41:14 GMT+0000 (Coordinated Universal Time)
cuid: clvwk5p0p000009jmgysz5jh7
slug: mastering-the-challenge-solve-longest-substring-without-repeating-characters-on-leetcode
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1715096200419/85f2d807-6b46-42de-956d-128f9f1a7cda.jpeg
tags: interview, python, interview-questions, leetcode, leetcode-solution

---

## Introduction to 'Longest Substring Without Repeating Characters'

When preparing for software engineering interviews, understanding how to tackle problems involving strings is crucial. Today, I'll walk you through the problem of finding the [longest substring without repeating characters (LeetCode 3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/), a common question in technical interviews, especially on platforms like LeetCode.

> Given a string `s`, find the length of the **longest substring** without repeating characters.
> 
> A **substring** is a contiguous **non-empty** sequence of characters within a string.
> 
> **Example 1:**
> 
> ```plaintext
> Input: s = "abcabcbb"
> Output: 3
> Explanation: The answer is "abc", with the length of 3.
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: s = "bbbbb"
> Output: 1
> Explanation: The answer is "b", with the length of 1.
> ```
> 
> **Example 3:**
> 
> ```plaintext
> Input: s = "pwwkew"
> Output: 3
> Explanation: The answer is "wke", with the length of 3.
> Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
> ```

## Different Approaches to Solve the Problem

To solve this problem, one might consider several strategies:

1. **Brute Force**: The simplest approach involves generating all possible substrings and checking each for uniqueness. This method, however, is highly inefficient (O(n^3) time complexity) due to the need to examine every substring and then check each for repeated characters.
    
2. **Sliding Window Using HashSet**: A more efficient approach uses the sliding window technique with a HashSet to track characters in the current substring. This method improves the time complexity to O(2n), which is better but can still be optimized.
    
3. **Optimized Sliding Window Using HashMap**: The optimal solution employs a sliding window along with a HashMap to remember the last index of each character. This refinement allows the window to skip redundant checks efficiently, bringing the complexity down to O(n).
    

## Creating the Optimal Solution

In the optimal approach, we use a HashMap to store the most recent index of each character as we iterate through the string. This way, if we encounter a character that is already in the HashMap, we can adjust the starting point of our window to the right of the last occurrence of that character, thus skipping over redundant parts of the string.

The key here is to keep expanding the window from the end until a repeat character is found, while simultaneously updating the starting point and the maximum length found so far.

The time complexity of this approach is O(n), where n is the length of the string. This is because each character in the string is processed once when it enters the window and once when it moves out (in the worst case).

### Python Solution

```python
def lengthOfLongestSubstring(s: str) -> int:
    used = {}  # This will map characters to their most recent index
    max_length = start = 0  # Initialize max_length and the start of the window

    for i, c in enumerate(s):
        # If the character is in the map and its index is within the current window
        if c in used and start <= used[c]:
            start = used[c] + 1  # Move the start right after the last occurrence
        else:
            max_length = max(max_length, i - start + 1)  # Update the max_length if the current window is larger

        used[c] = i  # Update the map with the current index of the character

    return max_length  # Return the maximum length found
```

## Conclusion

The problem of finding the longest substring without repeating characters is an excellent exercise for understanding string manipulation and optimizing algorithms using the sliding window technique.

By mastering this problem, you can confidently tackle similar string-based challenges in your interviews and beyond. Always remember to consider multiple approaches and understand their trade-offs to select the most efficient solution for your interview problems.