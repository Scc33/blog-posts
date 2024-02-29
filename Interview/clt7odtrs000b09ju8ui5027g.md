---
title: "Mastering the Mirror: A Deep Dive into Inverting Binary Trees for LeetCode Success"
seoTitle: "Binary Tree Inversion: Ace LeetCode with Python, Java, TS"
seoDescription: "Learn to flip binary trees for LeetCode success. This guide covers Python, TypeScript, and Java solutions with easy-to-understand explanations and analysis."
datePublished: Thu Feb 29 2024 20:25:52 GMT+0000 (Coordinated Universal Time)
cuid: clt7odtrs000b09ju8ui5027g
slug: mastering-the-mirror-a-deep-dive-into-inverting-binary-trees-for-leetcode-success
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1709238058071/eb2f1536-10a7-4e47-9255-2416d0cde97e.webp
tags: interview, java, python3, typescript, interview-tips

---

Today, I dive into a common yet intriguing problem often encountered on platforms like LeetCode: [inverting a binary tree (LeetCode 226)](https://leetcode.com/problems/invert-binary-tree/description/). This challenge not only tests your grasp of binary trees but also your ability to think recursively and iteratively.

Let's embark on this journey together, exploring the depths of the problem and unveiling solutions across three major programming languages.

---

## Introduction to the Problem

Imagine a binary tree where each node has up to two children. Inverting this tree means swapping every left child with its right child, all the way down the tree. It's akin to creating a mirror image of the tree across its central axis. For instance, if our original tree is visually represented as:

```markdown
     10
   /   \
  2     7
 / \   / \
1   3 6   9
```

After inversion, it would transform into:

```markdown
     10
   /   \
  7     2
 / \   / \
9   6 3   1
```

Such a transformation requires a systematic approach to traverse and swap the children of each node.

---

## Solving the Problem

To invert a binary tree, we can employ either recursion or iteration. The recursive approach involves a simple but elegant strategy: for each node, we swap its left and right children, then proceed to recursively invert the left and right subtrees. The base case for our recursion is when we encounter a null node, at which point we simply return without performing any inversion.

In terms of **Big O notation**, the time complexity of this algorithm is O(n), where n is the number of nodes in the tree. This is because we must visit each node exactly once to swap its children. The space complexity is O(h), where h is the height of the tree, accounting for the stack space used by recursion. In the worst case (a completely unbalanced tree), this could be O(n), but it's generally much less.

The iteration approach uses a queue data structure and is also O(n) runtime.

---

## Solution in Python

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty, return immediately
        if root is None:
            return None
        
        # Swap the left and right children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

---

## Solution in TypeScript

```typescript
function invertTree(root: TreeNode | null): TreeNode | null {
    // Base case: if the tree is empty, do nothing
    if (root === null) {
        return null;
    }
    
    // Swap the left and right children
    const temp = root.left;
    root.left = root.right;
    root.right = temp;
    
    // Recursively invert the left and right subtrees
    invertTree(root.left);
    invertTree(root.right);
    
    return root;
};
```

---

## Solution in Java

*With Recursion:*

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        // Recursively invert the subtrees
        invertTree(root.left);
        invertTree(root.right);
        
        // Swap the left and right children
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        return root;
    }
}
```

*Without Recursion (Iterative):*

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        if (root != null) {
            queue.add(root);
        }
        while (!queue.isEmpty()) {
            TreeNode current = queue.poll();
            // Swap the children
            TreeNode temp = current.left;
            current.left = current.right;
            current.right = temp;
            // Add children to the queue for later processing
            if (current.left != null) queue.add(current.left);
            if (current.right != null) queue.add(current.right);
        }
        return root;
    }
}
```

---

## Conclusion

Inverting a binary tree, while seemingly straightforward, encompasses critical concepts in tree manipulation and traversal techniques. Whether you prefer the elegance of recursion or the hands-on approach of iteration, mastering this problem will sharpen your problem-solving skills and prepare you for the challenges of software engineering interviews.

As you continue on your journey, remember that the beauty of coding lies not just in solving problems, but in crafting solutions that are both efficient and understandable.

Happy coding, and may your trees always be perfectly mirrored!