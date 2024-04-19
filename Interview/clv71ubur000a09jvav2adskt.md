---
title: "Mastering LeetCode: Converting Roman to Integer"
seoTitle: "Convert Roman to Integer - LeetCode Python Guide"
seoDescription: "Explore efficient strategies for converting Roman numerals to integers with our in-depth guide featuring Python, Java, and TypeScript solutions."
datePublished: Fri Apr 19 2024 19:14:16 GMT+0000 (Coordinated Universal Time)
cuid: clv71ubur000a09jvav2adskt
slug: mastering-leetcode-converting-roman-to-integer
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1713549619152/c1d17af3-3aa3-4bf6-a30c-b62e3073c66c.jpeg
tags: interview, javascript, python, typescript, leetcode

---

## Introduction to Roman Numerals Conversion

[Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals), a numeral system originating in ancient Rome, are used in various applications even today, from clock faces to movie release years. However, translating them into integers that modern computers can understand poses an interesting challenge ([LeetCode 13](https://leetcode.com/problems/roman-to-integer/description/)).

Roman numerals are composed of seven symbols each representing a fixed integer value. Numbers are generally formed by combining these symbols, following specific rules not only for addition but also for subtraction, making the system slightly complex but intriguing for algorithmic implementation.

> Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
> 
> ```plaintext
> Symbol       Value
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000
> ```
> 
> For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27`is written as `XXVII`, which is `XX + V + II`.
> 
> Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:
> 
> * `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
>     
> * `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
>     
> * `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.
>     
> 
> Given a roman numeral, convert it to an integer.
> 
> **Example 1:**
> 
> ```plaintext
> Input: s = "III"
> Output: 3
> Explanation: III = 3.
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: s = "LVIII"
> Output: 58
> Explanation: L = 50, V= 5, III = 3.
> ```
> 
> **Example 3:**
> 
> ```plaintext
> Input: s = "MCMXCIV"
> Output: 1994
> Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
> ```

## Analyzing Different Approaches

To solve the problem of converting Roman numerals to integers, one can consider multiple approaches:

1. **Sequential Parsing:** Start from the left, read each symbol, and add its value to the total. When a symbol smaller than its successor is found, subtract its value instead of adding it. This approach reflects the most direct interpretation of the rules.
    
2. **Replace and Sum:** Convert subtractive combinations (like IV or IX) into their additive equivalents (IIII or VIIII) before summing. This simplifies parsing but requires preprocessing the input string.
    
3. **Mapping and Lookup:** Use a dictionary to map each Roman numeral symbol to its value, enabling quick conversions and handling exceptions for subtractive cases as special conditions within the loop.
    

## Solution and Complexity Analysis

The optimal solution for both readability and performance is the Sequential Parsing approach. This method involves iterating over the string of Roman numerals, checking the value of the current symbol against the next symbol. If the current symbol's value is less than the next one, it indicates a subtractive combination, and we subtract rather than add the value.

### Complexity Analysis

* **Time Complexity:** O(n), where n is the length of the Roman numeral string. Each symbol is processed once.
    
* **Space Complexity:** O(1), as the extra space required is minimal and does not depend on the input size.
    

## Solutions

### Python Solution

```python
def romanToInt(s: str) -> int:
    translations = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = translations[char]
        if value >= prev_value:
            total += value  # Add the value if it's not a subtractive combination
        else:
            total -= value  # Subtract the value if it's a subtractive combination
        prev_value = value
    return total
```

### TypeScript Solution

```typescript
function romanToInt(s: string): number {
    const translations: { [key: string]: number } = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    };
    let total = 0;
    let prevValue = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        const value = translations[s.charAt(i)];
        if (value >= prevValue) {
            total += value;
        } else {
            total -= value;
        }
        prevValue = value;
    }
    return total;
}
```

### Java Solution

```java
public int romanToInt(String s) {
    int[] values = new int[s.length()];
    for (int i = 0; i < s.length(); i++) {
        values[i] = switch (s.charAt(i)) {
            case 'I' -> 1;
            case 'V' -> 5;
            case 'X' -> 10;
            case 'L' -> 50;
            case 'C' -> 100;
            case 'D' -> 500;
            case 'M' -> 1000;
            default -> 0;
        };
    }
    int total = 0;
    for (int i = 0; i < values.length - 1; i++) {
        if (values[i] < values[i + 1])
            total -= values[i];
        else
            total += values[i];
    }
    total += values[values.length - 1];
    return total;
}
```

### Python Solution #2

Finally, if you're feeling really sneaky, you can use replaces.

```python
def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        intNum = 0
        iSubtractions = s.replace("IV", "IIII").replace("IX", "VIIII")
        xSubtractions = iSubtractions.replace("XL", "XXXX").replace("XC", "LXXXX")
        cSubtractions = xSubtractions.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in cSubtractions:
            intNum += translations[char]
        return intNum
```

### Conclusion

Understanding and implementing the conversion of Roman numerals to integers exemplifies a basic yet critical algorithmic problem-solving skill. Each solution in Python, TypeScript, and Java highlighted here not only serves the functional requirement but also helps in grasping fundamental programming concepts like arrays, loops, and conditional logic.

For anyone preparing for software engineering interviews, mastering such problems is invaluable, enhancing both your problem-solving skills and your readiness for technical challenges.

Feel free to analyze, run, and modify the provided solutions as per your learning and testing needs. Happy coding!