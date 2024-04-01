---
title: "Mastering LeetCode: Unraveling the 'Same Tree' Problem"
seoTitle: "Crack LeetCode: Solve 'Same Tree' Easily"
seoDescription: "Master the 'Same Tree' problem on LeetCode with our guide. Get solutions in Python, TypeScript, and Java with clear, detailed explanations."
datePublished: Mon Apr 01 2024 16:50:50 GMT+0000 (Coordinated Universal Time)
cuid: cluh6sjrh000709jubaxm7eew
slug: mastering-leetcode-unraveling-the-same-tree-problem
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1711990188993/b6c9fdf3-f42e-4c3e-8833-18f5e4604618.webp
tags: java, javascript, python, typescript, leetcode

---

Let's dive deep into cracking one of LeetCode's intriguing problems: determining if two binary trees are the same ([LeetCode 100. Same Tree](https://leetcode.com/problems/same-tree/description/)). This challenge is not only a test of understanding binary tree structures but also an exercise in applying recursive solutions effectively.

## Introduction to the Problem

Imagine you're given two binary trees, `p` and `q`. Your task is straightforward yet tricky: write a function that checks if these trees are identical. By identical, we mean that the trees have the same structure, and each corresponding node across the trees shares the same value.

> Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
> 
> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
> 
> **Example 1:**
> 
> [![Same binary tree](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg align="center")](https://leetcode.com/problems/same-tree/description/)
> 
> ```plaintext
> Input: p = [1,2,3], q = [1,2,3]
> Output: true
> ```
> 
> **Example 2:**
> 
> [![Different binary trees](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg align="center")](https://leetcode.com/problems/same-tree/description/)
> 
> ```plaintext
> Input: p = [1,2], q = [1,null,2]
> Output: false
> ```
> 
> **Example 3:**
> 
> [![Different binary trees](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg align="center")](https://leetcode.com/problems/same-tree/description/)
> 
> ```plaintext
> Input: p = [1,2,1], q = [1,1,2]
> Output: false
> ```

## Strategy for Solution

The key to solving this problem lies in recursion—a fundamental technique where the solution involves solving smaller instances of the same problem. We'll compare the root values of `p` and `q`. If they match, we recursively check both the left and right subtrees. This process continues until either a mismatch is found or all nodes are verified to be identical.

The Big O notation for this algorithm is O(n), where n is the number of nodes in the tree. This is because, in the worst case, we must visit each node exactly once to compare its value with the corresponding node in the other tree.

## Python Solution

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Both nodes are None
            return True
        if not p or not q or p.val != q.val:  # One is None or values differ
            return False
        # Recursively check both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

## TypeScript Solution

For those who prefer TypeScript, the approach remains similar, adjusted for TypeScript syntax:

```typescript
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
```

## Java Solution

Finally, let's look at how to implement this in Java, keeping the logic consistent across languages:

```java
public class TreeNode {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

### Conclusion

Tackling the 'Same Tree' problem on LeetCode serves as an excellent practice for understanding binary trees and the power of recursion.

Whether you're new to engineering interviews or an experienced coder, mastering such problems will sharpen your problem-solving skills and prepare you for real-world challenges. Remember, the key is to break down the problem into smaller, manageable tasks and approach them systematically.

Happy coding!