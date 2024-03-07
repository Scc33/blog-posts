---
title: "Mastering LeetCode's "Lowest Common Ancestor in a BST": A Comprehensive Guide"
seoTitle: "Solve LCA on BST: LeetCode's Guide for All"
seoDescription: "Ace the LeetCode LCA in BST problem with our expert guide. Learn efficient solutions in Python, TypeScript, and Java to boost your interview skills."
datePublished: Thu Mar 07 2024 22:29:04 GMT+0000 (Coordinated Universal Time)
cuid: clthsv84k000709l0afi07ud3
slug: mastering-leetcodes-lowest-common-ancestor-in-a-bst-a-comprehensive-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1709850508164/86e438c9-534b-44a5-9f3f-f06d740b0a99.webp
tags: java, javascript, python3, leetcode, leetcode-solution

---

### **Introduction**

In the realm of software engineering interviews, understanding data structures and their related algorithms is paramount. A common question that arises is finding the [lowest common ancestor (LCA)](https://en.wikipedia.org/wiki/Lowest_common_ancestor) of two nodes in a [binary search tree (BST)](https://en.wikipedia.org/wiki/Binary_search_tree).

This problem, as defined by LeetCode, challenges us to identify the lowest node within a BST that has both given nodes as descendants, potentially including themselves as descendants. Imagine a BST with nodes 6, 2, 8, 0, 4, 7, and 9; if we were to find the LCA of nodes 2 and 8, the answer would be 6, illustrating a practical example of this concept.

[![Binary search tree example](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png align="center")](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

This is [**LeetCode 235: Lowest Common Ancestor of a Binary Search Tree**](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)**.**

## What Is a Binary Search Tree?

A binary search tree is a fundamental data structure where each node has at most two children, referred to as the left and right child. The BST is organized in such a way that for any given node, all elements in the left subtree are lesser, and those in the right subtree are greater. This property significantly optimizes search, insertion, and deletion operations, leveraging the tree's structure to reduce complexity.

## Understanding the Solution

Solving the LCA problem in a BST is intuitive once you grasp the BST's properties. The key is to utilize the fact that the tree is ordered. Starting from the root, if both nodes `p` and `q` are less than the current node, our LCA lies in the left subtree. Conversely, if `p` and `q` are greater, it lies in the right subtree. When `p` and `q` no longer satisfy these conditions, we've found our LCA.

This approach ensures an efficient traversal, with a time complexity of O(h), where h is the height of the tree.

## Python Solution

```python
class Solution:
    # Recursive approach to find LCA in a BST
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both p and q are lesser than root, LCA is in the left subtree
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q are greater than root, LCA is in the right subtree
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # We have found the LCA
        else:
            return root
```

## TypeScript Solution

```typescript
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (root === null) return null;
    // Navigate left if both nodes are lesser than root
    if (p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left, p, q);
    } 
    // Navigate right if both nodes are greater than root
    else if (p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right, p, q);
    } 
    // Current root is LCA
    else {
        return root;
    }
}
```

## Java Solution

Fun case where the Java and TypeScript are almost the exact same!

```java
public class Solution {
    // Utilizing BST properties to find the LCA
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // If both p and q are lesser, go left
        if (p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        } 
        // If both are greater, go right
        else if (p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        } 
        // Found the LCA
        else {
            return root;
        }
    }
}
```

## Conclusion

The Lowest Common Ancestor problem in a binary search tree offers a fantastic opportunity to deepen our understanding of BST operations and their applications in solving complex problems. By leveraging the BST's inherent structure, we can devise a solution that is both elegant and efficient.

Whether you're a seasoned engineer brushing up for interviews or new to the coding challenge arena, mastering such problems can significantly boost your confidence and skill set. Remember, the key to excelling in coding interviews is not just solving the problem but understanding the underlying principles that lead to the solution.