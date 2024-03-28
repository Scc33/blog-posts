---
title: "Mastering LeetCode: Crafting the Longest Palindrome from Mixed Letters"
seoTitle: "LeetCode Guide: Maximize Palindrome Length"
seoDescription: "Discover how to solve the LeetCode palindrome length problem with our in-depth guide, featuring Python, TypeScript, and Java solutions."
datePublished: Thu Mar 28 2024 01:30:59 GMT+0000 (Coordinated Universal Time)
cuid: cluak67bj000308l0hpg3hh4i
slug: mastering-leetcode-crafting-the-longest-palindrome-from-mixed-letters
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1711589336799/f3c30e49-dd23-4ad1-b9a7-16603ceb0234.webp
tags: java, javascript, python, leetcode, leetcode-solution

---

## Introduction

Imagine receiving a jumbled collection of letters, both uppercase and lowercase, with the challenge to arrange these into the longest possible palindrome. This problem isn't just a brain teaser; it’s a common question in software engineering interviews, exemplified by tasks like those found on LeetCode ([LeetCode 409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/)).

A [palindrome](https://en.wikipedia.org/wiki/Palindrome), as you may know, is a word or sequence that reads the same backward as forward, such as "radar" or "madam". The twist here is that "Aa" isn't a palindrome due to case sensitivity. Through examples like "abccccdd" transforming into "dccaccd" (7 characters) and "a" standing alone as "a" (1 character), we uncover the essence of this intriguing problem.

> Given a string `s` which consists of lowercase or uppercase letters, return *the length of the* ***longest palindrome*** that can be built with those letters.
> 
> Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.
> 
> **Example 1:**
> 
> ```plaintext
> Input: s = "abccccdd"
> Output: 7
> Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: s = "a"
> Output: 1
> Explanation: The longest palindrome that can be built is "a", whose length is 1.
> ```

## The Strategy for Solution

To tackle this problem, one must think about the characteristics of a palindrome: it is symmetrical. Each letter on one side has a matching letter on the opposite side, except possibly for one letter in the center of an odd-length palindrome. This insight leads us to focus on pairing up letters while possibly leaving one unpaired for the center.

The crux of the solution lies in tracking letters that cannot be paired yet. Utilizing a set for this purpose is efficient: when we encounter a letter, if it's not in the set, we add it, indicating it's unpaired. If it is in the set, we remove it, signifying we've found its pair. After iterating through all letters, if there are unpaired letters left, we can only use one of them in the center of our palindrome, hence the adjustment of subtracting the count of unpaired letters from the total length of the string and adding one.

This leads to an algorithm with a time complexity of O(n), where n is the length of the string, as we need to examine each letter.

## Python Solution

```python
def longestPalindrome(s: str) -> int:
    non_paired_letters = set()
    for letter in s:
        if letter not in non_paired_letters:
            non_paired_letters.add(letter)
        else:
            non_paired_letters.remove(letter)
    # Use all letters except for the unpaired ones, plus one for the center if needed.
    return len(s) - len(non_paired_letters) + 1 if non_paired_letters else len(s)
```

This Python solution employs a set to keep track of unpaired letters, elegantly achieving the goal with minimal overhead.

## TypeScript Solution

```typescript
function longestPalindrome(s: string): number {
    let nonPairedLetters: Set<string> = new Set();
    for (let letter of s) {
        if (!nonPairedLetters.has(letter)) {
            nonPairedLetters.add(letter);
        } else {
            nonPairedLetters.delete(letter);
        }
    }
    let adjustments: number = nonPairedLetters.size ? 1 : 0;
    return s.length - nonPairedLetters.size + adjustments;
}
```

In TypeScript, the approach mirrors the Python solution, utilizing a set to track unpaired letters and making a simple adjustment for the potential center letter.

## Java Solution

```java
public int longestPalindrome(String s) {
    Set<Character> nonPairedLetters = new HashSet<>();
    for (int i = 0; i < s.length(); i++) {
        char letter = s.charAt(i);
        if (!nonPairedLetters.contains(letter)) {
            nonPairedLetters.add(letter);
        } else {
            nonPairedLetters.remove(letter);
        }
    }
    int adjustments = nonPairedLetters.isEmpty() ? 0 : 1;
    return s.length() - nonPairedLetters.size() + adjustments;
}
```

The Java version employs a `HashSet` to keep track of unpaired characters, with logic similar to that of Python and TypeScript, emphasizing the universality of this solution across languages.

### Conclusion

Solving the longest palindrome problem provides a fascinating glimpse into the efficiency and elegance of using data structures like sets in programming. Whether in Python, TypeScript, or Java, the principle remains the same: pair up letters and account for a potential central character. This approach not only solves the problem but also showcases the kind of logical thinking and algorithmic efficiency prized in software engineering interviews.

As you continue to prepare for these challenges, remember that understanding the problem and employing simple, effective strategies can lead to solutions that are both elegant and efficient.