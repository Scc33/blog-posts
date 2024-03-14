---
title: "Mastering the Staircase: Dynamic Programming Solutions for LeetCode's Climbing Stairs Problem"
seoTitle: "Solve LeetCode's Staircase with Dynamic Programming"
seoDescription: "Discover how to crack the LeetCode Climbing Stairs problem using dynamic programming, with step-by-step solutions in Python, TypeScript, and Java."
datePublished: Thu Mar 14 2024 02:24:05 GMT+0000 (Coordinated Universal Time)
cuid: cltqlwk6u000509jr7bpn7iq6
slug: mastering-the-staircase-dynamic-programming-solutions-for-leetcodes-climbing-stairs-problem
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1710383020032/3fc0075a-469e-438c-864d-90301a0bbb13.webp
tags: python, leetcode, dynamic-programming, leetcodedaily, leetcode-solution

---

In the realm of software engineering interviews, the "Climbing Stairs" problem is a classic question that often surfaces, especially on platforms like LeetCode ([LeetCode 70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)).

It's an excellent way for interviewers to assess a candidate's grasp of dynamic programming. Let me walk you through this intriguing problem, explain what dynamic programming is, and how to solve this problem efficiently.

## Introduction to the Problem

Imagine you're standing at the base of a staircase with `n` steps. You can move up the staircase by taking either one step or two steps at a time. The question then is: How many distinct ways can you climb to the top?

For instance, if the staircase has 2 steps (`n = 2`), there are two ways to reach the top:

1. Take one step twice (1 step + 1 step)
    
2. Take two steps once (2 steps)
    

And if the staircase has 3 steps (`n = 3`), there are three ways to climb to the top:

1. Take one step three times (1 step + 1 step + 1 step)
    
2. Take one step, then two steps (1 step + 2 steps)
    
3. Take two steps, then one step (2 steps + 1 step)
    

> You are climbing a staircase. It takes `n` steps to reach the top.
> 
> Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?
> 
> **Example 1:**
> 
> ```markdown
> Input: n = 2
> Output: 2
> Explanation: There are two ways to climb to the top.
> 1. 1 step + 1 step
> 2. 2 steps
> ```
> 
> **Example 2:**
> 
> ```markdown
> Input: n = 3
> Output: 3
> Explanation: There are three ways to climb to the top.
> 1. 1 step + 1 step + 1 step
> 2. 1 step + 2 steps
> 3. 2 steps + 1 step
> ```

## What is Dynamic Programming?

[Dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming) is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for solving problems where the same subproblem occurs multiple times. By solving each subproblem only once and storing its result, dynamic programming reduces the number of calculations needed, thereby optimizing the overall solution process.

## Solving the Problem with an Array (O(n) Space Solution)

To solve the "Climbing Stairs" problem using dynamic programming, we can start by recognizing that the number of ways to reach the `n`th step is the sum of ways to reach the `(n-1)`th and `(n-2)`th steps. This leads us to a bottom-up approach where we calculate the solution step by step, starting from the base cases.

**Big O Notation Analysis**: This approach has a time complexity of O(n) and a space complexity of O(n) due to the use of an array to store the results of subproblems.

Here's how you can implement this solution in Python:

```python
def climbStairs(n: int) -> int:
    if n <= 1:
        return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Optimizing the Solution to O(1) Space

While the above solution is efficient, we can further optimize the space complexity to O(1) by realizing that we only need to keep track of the last two steps at any point in time.

### Python Solution

```python
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    one_step_before, two_steps_before = 2, 1
    for i in range(2, n):
        all_ways = one_step_before + two_steps_before
        two_steps_before, one_step_before = one_step_before, all_ways
    return one_step_before
```

### TypeScript Solution

```typescript
function climbStairs(n: number): number {
    if (n === 1) return 1;
    let one_step_before = 2;
    let two_steps_before = 1;
    for (let i = 2; i < n; i++) {
        let all_ways = one_step_before + two_steps_before;
        [two_steps_before, one_step_before] = [one_step_before, all_ways];
    }
    return one_step_before;
}
```

### Java Solution

```java
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        int one_step_before = 2;
        int two_steps_before = 1;
        for (int i = 2; i < n; i++) {
            int all_ways = one_step_before + two_steps_before;
            two_steps_before = one_step_before;
            one_step_before = all_ways;
        }
        return one_step_before;
    }
}
```

## Conclusion

Dynamic programming is a powerful technique that can simplify and speed up solutions to problems like the Climbing Stairs puzzle. By understanding and applying dynamic programming principles, you can efficiently solve problems with overlapping subproblems and optimal substructure, a common theme in software engineering interviews.

Whether you're an experienced engineer or new to engineering interviews, mastering dynamic programming will undoubtedly be a valuable asset in your toolkit.

Remember, the journey of mastering dynamic programming is much like climbing stairs: one step at a time. Happy coding!

---

I hope this post helps you grasp the Climbing Stairs problem and the dynamic programming technique. Your feedback and questions are always welcome, as they inspire me to share more insights and solutions. Thank you for your kind words and encouragement!