---
title: "Find the Index of the First Occurrence in a String (Naive and KMP Solutions)"
seoTitle: "Index First Occurrence in String"
seoDescription: "Find first occurrence of a string in Python using naive and KMP solutions."
datePublished: Wed Apr 05 2023 20:56:51 GMT+0000 (Coordinated Universal Time)
cuid: clg466jpm00020al3hpyi896v
slug: find-the-index-of-the-first-occurrence-in-a-string-naive-and-kmp-solutions
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1680705349586/37f7831c-f7f2-493b-9810-952266bfa235.png
tags: interview, python, leetcode, leetcode-solution, interview-preparations

---

## Problem

Let's take a look at the problem [Find the Index of the First Occurance in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/).

In this problem, you have two strings: a needle and a haystack. The goal is to return the index of the needle in the haystack or -1 if the needle does not exist in the haystack.

This is a Leetcode easy-level problem. I think the naive solution fits that definition, however as you will see, the faster runtime solution requires some heavy lifting. That solution makes it feels more like a medium problem to me.

I'll be tackling this problem using Python.

## Naive Solution

First, let's consider the naive solution. At the very basic level, we can use the [built-in find function](https://www.w3schools.com/python/ref_string_find.asp).

```python
class Solution(object):
    def strStr(self, haystack, needle):
    	    return haystack.find(needle)
```

If you don't have access to *find* or are a Python warrior and want to grind things out, then you could implement the following.

```python
class Solution(object):
    def strStr(self, haystack, needle):
        searchLen = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+searchLen] == needle:
                return i
        return -1
```

This line uses string slicing to extract a substring of length `searchLen` starting at the current index `i` of the `haystack` string, and then checks if it matches the `needle` string. If there's a match, the function returns the current index `i`. If we reach the end of the `haystack` then we return `-1` as the needle was not found.

### Naive Solution Runtime

Assume *m* is the length of the haystack and *n* is the length of the needle. We are looping over the entire length of the haystack giving at least *O(m).* In each iteration, we are taking a substring and comparing it to the needle which gives O(*n)*. Therefore, the overall time complexity of this Naive solution is ***O(mn)***.

## KMP Solution

*O(mn)* isn't a very good solution and we can certainly do better by using an algorithm known as Knuth–Morris–Pratt or simply KMP. Before diving into code, it is helpful to understand what KMP is, so let's look at some definitions.

ChatGPT describes KMP as the following.

> The Knuth-Morris-Pratt (KMP) algorithm is a string-matching algorithm that searches for occurrences of a pattern within a longer text. It was developed by Donald Knuth, Vaughan Pratt, and James Morris in 1977.
> 
> The KMP algorithm uses a pre-processing step to build a partial match table, which is used to determine the largest possible suffix of the pattern that matches a prefix of the text. This information is then used to avoid unnecessary comparisons when searching for occurrences of the pattern within the text.
> 
> The KMP algorithm has a time complexity of O(m + n), where m is the length of the pattern and n is the length of the text. This makes it more efficient than other string-matching algorithms such as the naive algorithm, which has a time complexity of O(m \* n).
> 
> Overall, the KMP algorithm is a useful tool for applications such as text search, data compression, and bioinformatics.

Thank you GPT. However, I prefer [Wikipedia's more succinct KMP description](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm).

> \[KMP Algorithm\] searches for occurrences of a "word" `W` within a main "text string" `S` by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.

Finally, let's consider one last definition from [GeeksForGeeks](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/).

> The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match.

Equipped with these three definitions of KMP we can begin to see this technique offers a speed-up because we avoid unnecessary comparisons on each iteration over the haystack.

The key leverage point needed to make this speed up is that we will use a helper array to do prefix and suffix matching.

### KMP Implementation

```python
class Solution(object):
    def strStr(self, haystack, needle):
        needleLen = len(needle)
        haystackLen = len(haystack)
        i = 1
        j = 0
        patternArr = [-1] + [0] * needleLen
        while i < needleLen:            # calculate helper array
            if j == -1 or needle[i] == needle[j]:   
                i += 1
                j += 1
                patternArr[i] = j
            else:
                j = patternArr[j]
        i = 0
        j = 0
        while i < haystackLen and j < needleLen:  # process haystack with helper array
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = patternArr[j]
        if j == needleLen: 
            return i-j
        else: 
            return -1
```

First, we set up the necessary variables including the length of the needle, the length of the haystack, and the pattern array that we will use to speed up matching.

Next, we loop over the needle string. `i` leads and will always be ahead while `j` follows (because `i` starts at one and `j` starts at zero). If there is a match then we write the value of `j` into the helper/pattern array at `i`. You can think of a match as when some part of the suffix is the same as some part of the prefix.

After populating the helper array we can finally look through the haystack for a match. In this loop, `i` will represent our place in the haystack and `j` our position in the needle. I've used the same variable names for brevity but you could easily name them something else if that helps you understand and document your code.

If there is a match between the haystack and the needle we increment both counters, otherwise we reset `j` to the previous value in the pattern array.

If `j` equals the length of the needle then we know we have matched the entire needle. The location of the needle in the haystack is calculated by `i-j`. Otherwise, if no needle is found and we will return -1 to indicate that there is no match.

### Example Execution

That is a fairly complex piece of code so let's set through it to see how the parts are working together.

Suppose we have the needle `abac` and the haystack of `abyabgabac`.

Upon processing the needle we will generate the following helper array.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1680707435645/0cadf349-8118-45aa-97d9-b41c63fa9b97.png align="center")

The one and two underneath the second `ab` represent a match between that suffix and the earlier prefix `ab`. Now we use that array to process the haystack.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1680708215104/aa779722-48f7-48a8-801e-f5626c1e810b.png align="center")

Notice the `i` counter variable which is tracking our position in the haystack is monotonically increasing while the `j` value jumps around. The `j` value is jumping around because it is tracking how much of a match we have seen. If we reach the end of the haystack and `j` equals the length of the needle that means we have seen a complete match.

If you want to see more examples I would recommend adding print statements to the code snippet above. Seeing the output of `i` and `j` on different inputs is really helpful for understanding this problem.

### KMP Solution Runtime

Assume *m* is the length of the haystack and *n* is the length of the needle. At the start, we calculate the needle suffix array which is *O(n).* Then we loop over the entire length of the haystack which is *O(m).* Therefore, the overall time complexity of the KMP solution is *O(m + n)*.

By taking this more advanced approach we have sped up the big O runtime from *O(mn)* to *O(m + n)*. Not too bad for a day's work.

## Where to Learn More

If you find video explanations helpful then I would highly recommend [this video by Coding Made Simple](https://www.youtube.com/watch?v=GTJr8OvyEVQ).

You can also read more interview prep with my [series on SWE interviewing](https://blog.seancoughlin.me/series/interview-prep).

The cover image was generated using [Dalle2](https://openai.com/product/dall-e-2) and the prompt "binary on a computer screen."