---
title: "How to Determine Valid Parentheses"
seoTitle: "How to Solve the Valid Parentheses Leetcode Problem"
seoDescription: "Learn how to determine valid parentheses in a string with a simple solution using a dictionary for efficient and compressed conditional logic."
datePublished: Sat Apr 08 2023 19:21:23 GMT+0000 (Coordinated Universal Time)
cuid: clg8d3c1t000409l49rvsdved
slug: how-to-determine-valid-parentheses
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1680966029154/db7797d3-2718-4561-b861-da10097e4a9a.png
tags: interview, software-engineering, leetcode, leetcodedaily, leetcode-solution

---

## The Problem

With this article, I will be covering the [Leetcode Valid Parentheses problem](https://leetcode.com/problems/valid-parentheses/description/). Leetcode describes the problem with the following.

> Given a string s containing just the characters '(', ')', '{', '}', '\[' and '\]', determine if the input string is valid.
> 
> An input string is valid if:
> 
> 1. Open brackets must be closed by the same type of brackets.
>     
> 2. Open brackets must be closed in the correct order.
>     
> 3. Every close bracket has a corresponding open bracket of the same type.
>     

One key note in the problem description is that the string `s` will only contain parenthesis-type characters. This simplification makes the problem easier because we only need to worry about six characters and don't have any concerns with trimming or stripping out irrelevant characters.

With this problem, and with most coding challenges, I followed a three-step process:

1. First, I like to understand the problem with an incorrect solution
    
2. Then I'll determine a solution that works
    
3. Finally, I'll optimize that solution to be fast and clean
    

With that framework, let's get into tackling this problem using Python.

## <s>Solution 1</s> - Getting Things Wrong

My kneejerk reaction was to count the number of parenthesis types. Since every opening parenthesis type will need a corresponding closing parenthesis, the counts need to be equal.

```python
# Note - this doesn't work
class Solution(object):
    def isValid(self, s):
        stack = []
        for letter in s:
            stack.append(letter)
        forwardParen = 0
        backwardParen = 0
        forwardCurly = 0
        backwardCurly = 0
        forwardSquare = 0
        backwardSquare = 0
        while stack:
            letter = stack.pop()
            if letter == '(':
                forwardParen += 1
            elif letter == ')':
                backwardParen += 1
            elif letter == '{':
                forwardCurly += 1
            elif letter == '}':
                backwardCurly += 1
            elif letter == '[':
                forwardSquare += 1
            else:
                backwardSquare += 1
        valid = forwardParen == backwardParen and forwardCurly == backwardCurly and forwardSquare == backwardSquare
        return valid # this solution will not work
```

This is a nice starting point, however, this solution is inaccurate. An example like `[(])` has an equivalent number of each type, but the alignment of those types does not form a valid set of parentheses.

Coming up with an incorrect solution is an *okay* way to start. An incorrect solution is often a good way to organize thoughts, understand the problem better, and rule out possibilities. From an incorrect solution, we can continue to optimize until we have something correct. Then from a correct solution, we can optimize further until we have a fast solution.

In this incorrect first step, I came across the kernel of understanding that leads to a solution. A stack.

## Solution 2 - Finding the Answer

The stack data structure will allow us to maintain the ordering of the characters in the string. For our stack, we will append each forward character. For example, `[({})]` would produce:

1. `{`
    
2. `(`
    
3. `[`
    

For any non-forward characters, we will pop the stack and compare if there is a match between our position in the string and the character in the stack we can continue onwards. If there is a mismatch then we know this isn't valid, and we can return false.

Using our previous example. The `}` matches the `{` on the top of the stack. Then `)` matches the `(` that follows on the stack. And finally, `]` matches `[` which is the last value in the stack. Since the stack is empty we know we have a valid string.

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    value = stack.pop()
                    if value == '(' and i != ')':
                        return False
                    elif value == '{' and i != '}':
                        return False
                    elif value == '[' and i != ']':
                        return False
        return len(stack) == 0
```

## Final Optimized Solution

I think the second solution is good, however, we can do better by incorporating a dictionary. Using a dictionary will allow for the compression of all the messy conditional logic into one simple check using the `in` keyword.

```python
class Solution(object):
    def isValid(self, s):
        parens = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in parens:
                stack.append(i)
            elif len(stack) == 0 or parens[stack.pop()] != i:
                return False
        return len(stack) == 0
```

First, define a dictionary containing forward parentheses as the key and backward parentheses as the value. Once again we will also need a stack.

Once we have the dictionary and a stack we can start our iteration over the string. If a character is in the dictionary then we add that to the stack. Here a character being in the dictionary implies that it is a forward character. If a character doesn't fit that description we drop to that second conditional.

The first condition in the elif covers cases when there is no opening character to a backward. For example, `))))))` has all backward characters and no forward characters. That will cause the stack to be empty, and then we know that this would not be a valid string.

The second condition in the elif covers mismatches in the ordering. For example, `{(})[]` has the correct number of forward and backward characters, but the ordering isn't valid. Here the `{` would be added to the stack and then `(` would follow. However, once we hit `}` then `(` would be popped from the stack. That does not match, so we bomb out and return false.

Finally, we return if the stack is empty or not. For example, the string `{` doesn't have a closing counterpart, so the stack would not be empty and that would not be a valid string. And that's it, the solution is complete!

### Big O Calculation

Lookups in our dictionary are *O(1)*. Appending to and popping from the array, which we are using as the underlying data structure for the stack, is also [*O(1)*](https://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python). We loop over the entire string so that is *O(n)*. Therefore the overall runtime is ***O(n)***.

## Where to Learn More

You can also read more interview prep with my [series on SWE interviewing](https://blog.seancoughlin.me/series/interview-prep).

The cover image was generated using [Dalle2](https://openai.com/product/dall-e-2) and the prompt “create an image incorporating mathematical symbols and a lot of parentheses in an impressionist style.”