---
title: "Valid Parentheses: A Leetcode Solution Guide"
seoTitle: "Crack Valid Parentheses: Leetcode Solution"
seoDescription: "Master the Valid Parentheses problem with our expert guide. Learn to solve it in Python, TypeScript, and Java with detailed code explanations."
datePublished: Wed Feb 28 2024 14:52:52 GMT+0000 (Coordinated Universal Time)
cuid: clt5x1q4z00060ajwamet6ot4
slug: valid-parentheses-a-leetcode-solution-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1709131862575/8b80d728-d1e3-4554-8f68-ff0f51011ab9.webp
tags: interview, java, javascript, python, interview-questions

---

Today, we're tackling a classic yet crucial problem that surfaces in many software engineering interviews: validating a string of brackets ([Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)). Let's dive in, ensuring we cover all necessary details and analyses.

## Introduction to the Problem

The problem at hand involves checking if a string containing only the characters '(', ')', '{', '}', '\[' and '\]' is valid based on three rules:

1. Open brackets must be closed by the same type of brackets.
    
2. Open brackets must be closed in the correct order.
    
3. Every close bracket has a corresponding open bracket of the same type.
    

This challenge is a litmus test for your understanding of basic data structures and algorithmic logic.

> **Example 1:**
> 
> ```markdown
> Input: s = "()"
> Output: true
> ```
> 
> **Example 2:**
> 
> ```markdown
> Input: s = "()[]{}"
> Output: true
> ```
> 
> **Example 3:**
> 
> ```markdown
> Input: s = "(]"
> Output: false
> ```

## How to Solve the Problem

The essence of solving this problem lies in using a stack, a data structure that operates on a [Last In, First Out (LIFO)](https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/) principle. Here's the approach:

1. Iterate through each character in the string.
    
2. If it's an opening bracket, push it onto the stack.
    
3. If it's a closing bracket, check if it matches the top item of the stack. If it does, pop the top item off the stack; otherwise, the string is invalid.
    
4. After processing all characters, if the stack is empty, the string is valid; if not, it's invalid.
    

### Big O Notation Analysis

The time complexity of this algorithm is O(n), where n is the length of the string. This is because we iterate through each character exactly once.

The space complexity is also O(n), in the worst-case scenario where all characters are opening brackets and get pushed onto the stack.

## Solution in Python

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack
        d = {'(':')', '{': '}', '[':']'}  # Mapping of brackets for easy lookup
        for c in s:
            if c in d:  # If it's an opening bracket, push to stack
                stack.append(c)
            elif len(stack) == 0 or d[stack.pop()] != c:  # If stack is empty or brackets don't match, return False
                return False
        return len(stack) == 0  # If stack is empty, all brackets were properly closed
```

## Solution in TypeScript

```typescript
function isValid(s: string): boolean {
    const stack: string[] = [];  // Initialize an empty stack
    let dict: { [key: string]: string } = {'{': '}', '[': ']', '(': ')'};  // Mapping of brackets
    for (let c of s) {
        if (dict.hasOwnProperty(c)) {  // If opening bracket, push to stack
            stack.push(c);
        } else if (stack.length === 0 || dict[stack.pop()] != c) {  // If stack is empty or brackets don't match, return False
            return false;
        }
    }
    return stack.length === 0;  // If stack is empty, all brackets were properly closed
}
```

## Solution in Java

Here's how you can tackle the problem in Java, adhering to the same logic:

```java
import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();  // Create a new stack
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(': 
                case '{': 
                case '[': 
                    stack.push(c); break;  // Push opening brackets onto the stack
                case ')': 
                    if (stack.isEmpty() || stack.pop() != '(') return false; break;  // Check for matching brackets
                case '}': 
                    if (stack.isEmpty() || stack.pop() != '{') return false; break;
                case ']': 
                    if (stack.isEmpty() || stack.pop() != '[') return false; break;
            }
        }
        return stack.isEmpty();  // Check if the stack is empty
    }
}
```

## Conclusion

Validating bracket sequences is a fundamental problem that beautifully illustrates the utility of the stack data structure in managing nested or sequential data in a LIFO manner.

By walking through the solutions in Python, TypeScript, and Java, we've not only explored how to approach and solve the problem but also how to analyze and understand its computational complexity.

Remember, mastering these concepts is key to excelling in software engineering interviews.