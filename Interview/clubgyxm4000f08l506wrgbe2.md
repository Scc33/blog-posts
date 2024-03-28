---
title: "Cracking the Code: Mastering Binary Summation on LeetCode"
seoTitle: "Binary String Addition: LeetCode Made Easy"
seoDescription: "Master binary string addition with our in-depth guide. Solutions in Python, TypeScript, and Java with full explanations and Big O analysis."
datePublished: Thu Mar 28 2024 16:49:07 GMT+0000 (Coordinated Universal Time)
cuid: clubgyxm4000f08l506wrgbe2
slug: cracking-the-code-mastering-binary-summation-on-leetcode
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1711643199098/1fb2b275-0ba2-4f2b-a58d-42559db6566c.webp
tags: java, javascript, python3, leetcode, leetcode-solution

---

In the realm of software engineering interviews, the mastery of algorithmic challenges forms the bedrock of a successful candidate's arsenal. Among these challenges, the task of summing binary strings stands out for its blend of simplicity and the foundational understanding of binary operations it requires.

Let's delve into a common problem encountered on platforms like LeetCode: given two binary strings, our goal is to return their sum as a binary string ([LeetCode 67. Add Binary](https://leetcode.com/problems/add-binary/description/)).

For example, consider the inputs "11" and "1". The sum of these binary strings is "100". Similarly, adding "1010" and "1011" yields "10101". At first glance, this task might seem straightforward, yet it encapsulates critical concepts crucial for binary arithmetic operations.

> Given two binary strings `a` and `b`, return *their sum as a binary string*.
> 
>  **Example 1:**
> 
> ```plaintext
> Input: a = "11", b = "1"
> Output: "100"
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: a = "1010", b = "1011"
> Output: "10101"
> ```

## Understanding the Solution

The crux of solving this problem lies in the binary addition algorithm, akin to the way we perform addition in decimal numbers, but with a binary twist. We start from the least significant bit, which is the rightmost bit of each binary string, and proceed towards the most significant bit, carrying over any excess to the next position.

Here's a step-by-step breakdown:

1. **Initialize a carry variable** to keep track of any overflow.
    
2. **Iterate from the rightmost bit to the left** for both binary strings. If one string is shorter, we consider its missing bits as 0.
    
3. **Add the corresponding bits** of both strings to the carry.
    
4. **Compute the sum's bit** by taking the modulo of the total by 2, and **update the carry** by dividing the total by 2.
    
5. **Append the computed bit** to the result.
    
6. **Reverse the result string** before returning, as we've built it backwards.
    

The **Big O notation** for this algorithm is **O(n)**, where **n** is the length of the longer binary string. This efficiency stems from the single-pass nature of our algorithm, directly correlating to the maximum length of the input strings.

## The Solutions

### Python Solution

```python
def addBinary(a: str, b: str) -> str:
    summation = []  # Stores the sum bits
    carry = 0  # Tracks the carry-over
    a_pointer = len(a) - 1  # Starts from the end of string a
    b_pointer = len(b) - 1  # Starts from the end of string b

    # Loop until both pointers are exhausted and no carry remains
    while a_pointer >= 0 or b_pointer >= 0 or carry:
        if a_pointer >= 0:
            carry += int(a[a_pointer])  # Add bit from a
            a_pointer -= 1
        if b_pointer >= 0:
            carry += int(b[b_pointer])  # Add bit from b
            b_pointer -= 1
        summation.append(str(carry % 2))  # Compute the bit to add to the sum
        carry //= 2  # Update carry

    return ''.join(reversed(summation))  # Reverse the sum to get the correct order
```

### TypeScript Solution

```typescript
function addBinary(a: string, b: string): string {
    let result: string[] = [];
    let carry: number = 0;
    let i: number = a.length - 1, j: number = b.length - 1;

    while (i >= 0 || j >= 0 || carry > 0) {
        let sum: number = carry;
        if (i >= 0) sum += parseInt(a[i--], 10); // Add bit from a
        if (j >= 0) sum += parseInt(b[j--], 10); // Add bit from b
        result.unshift((sum % 2).toString()); // Prepend the result with the current bit
        carry = Math.floor(sum / 2); // Calculate the new carry
    }

    return result.join('');
}
```

### Java Solution

```java
public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0'; // Subtract '0' to convert char to int
            if (j >= 0) sum += b.charAt(j--) - '0';
            sb.append(sum % 2); // Append the result bit
            carry = sum / 2; // Update the carry
        }
        
        return

 sb.reverse().toString(); // Reverse for correct order
    }
}
```

## Conclusion

The beauty of tackling this problem across multiple programming languages lies in understanding the universal principles of binary addition and adapting them to the syntax and idioms of each language.

Whether you're preparing for your next software engineering interview or simply brushing up on your programming skills, mastering such problems will undoubtedly sharpen your algorithmic thinking and enhance your problem-solving repertoire.

Remember, every line of code you write not only solves the problem at hand but also sows the seeds for your growth as a software engineer. Keep coding, keep learning, and let's decode the challenges together.