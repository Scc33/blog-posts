---
title: "Mastering LeetCode: Binary Search Tree Validation"
seoTitle: "Validating Binary Search Trees: Python Techniques"
seoDescription: "Learn methods to verify Binary Search Trees in Python with recursive, in-order traversal, and iterative approaches."
datePublished: Fri Jun 28 2024 17:54:08 GMT+0000 (Coordinated Universal Time)
cuid: clxyzsx5t000s08jq60m4f685
slug: mastering-leetcode-binary-search-tree-validation
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1719596733519/40d49456-e7c9-49b4-aec8-63103914280d.webp
tags: interview, algorithms, python, leetcode, leetcode-solution

---

## Introduction

[Binary Search Trees (BSTs)](https://www.google.com/search?client=safari&rls=en&q=binary+search+tree&ie=UTF-8&oe=UTF-8) are a fundamental data structure in computer science, widely used in various applications such as databases, searching algorithms, and more. Ensuring that a tree maintains the properties of a BST is crucial for the efficiency and correctness of these applications.

In this post, we will explore different techniques to validate whether a given binary tree is a BST using Python. We will cover the recursive approach, in-order traversal approach, and iterative approach, providing detailed explanations and code implementations for each method.

### **Validate Binary Search Tree LeetCode**

This post is based on [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) [**Validate Binary Search Tree**](https://leetcode.com/problems/validate-binary-search-tree/)**.**

> [Given the `root` of a bin](https://leetcode.com/problems/validate-binary-search-tree/)ary tree, *determine if it is a valid binary search tree (BST)*.
> 
> A **valid BST** is defined as follows:
> 
> * The left subtree of a node contains only nodes with keys **less than** the node's key.
>     
> * The right subtree of a node contains only nodes with keys **greater than** the node's key.
>     
> * Both the left and right subtrees must also be binary search trees.
>     

### What is a Binary Search Tree (BST)?

A Binary Search Tree is a tree data structure where each node has at most two children, referred to as the left and right child. The properties of a BST are as follows:

* **Left Subtree**: The left subtree of a node contains only nodes with keys less than the node’s key.
    
* **Right Subtree**: The right subtree of a node contains only nodes with keys greater than the node’s key.
    
* **Subtree Validity**: Both the left and right subtrees must also be binary search trees.
    

These properties ensure that operations like search, insert, and delete can be performed efficiently. Here is a visual example of a BST:

```plaintext
    5
   / \
  3   7
 / \ / \
2  4 6  8
```

### Practical Examples and Edge Cases

Let's consider some practical examples and edge cases:

**Example 1:** Input: `root = [2, 1, 3]`

```plaintext
    2
   / \
  1   3
```

Output: `True`

**Example 2:** Input: `root = [5, 1, 4, None, None, 3, 6]`

```plaintext
    5
   / \
  1   4
     / \
    3   6
```

Output: `False`

Explanation: The right child of the root node (4) is not greater than the root node (5).

### Why Validate a Binary Search Tree?

Validating a BST is important to ensure the integrity of the tree structure, which directly impacts the efficiency of operations performed on the tree. In scenarios such as database indexing or maintaining sorted data, an invalid BST can lead to incorrect results and degraded performance. Therefore, it is essential to have robust methods to validate the structure of a BST.

## Recursive Approach to Validate a BST

The recursive approach to validating a BST involves checking whether each node's value falls within a specific range defined by its ancestors. The initial range for the root node is `(-∞, ∞)`, and it gets updated as we traverse the tree.

#### Code Implementation

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        # An empty tree is a valid BST
        if not node:
            return True
        
        # The current node's value must be between low and high
        if not (low < node.val < high):
            return False
        
        # Recursively validate the left and right subtrees
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    
    return validate(root, float('-inf'), float('inf'))
```

#### Step-by-Step Breakdown

1. **TreeNode Class**: Defines the structure of a tree node with attributes for value, left child, and right child.
    
2. **is\_valid\_bst Function**: This function initiates the validation process.
    
3. **validate Helper Function**: Recursively checks each node:
    
    * **Base Case**: An empty node is considered valid.
        
    * **Value Check**: Ensures the current node’s value is within the specified bounds.
        
    * **Recursive Calls**: Validates the left subtree with an updated high bound (current node’s value) and the right subtree with an updated low bound (current node’s value).
        

#### Handling Edge Cases

* **Empty Tree**: An empty tree is a valid BST.
    
* **Single Node Tree**: A single-node tree is also a valid BST.
    
* **Imbalanced Tree**: The recursive approach correctly handles imbalanced trees by validating each subtree independently.
    

## In-Order Traversal Approach

An in-order traversal of a BST should yield values in a strictly increasing order. This property can be used to validate the tree by ensuring the values visited during in-order traversal are in ascending order.

#### Code Implementation

```python
def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    stack = []
    current = root
    prev_value = float('-inf')
    
    while stack or current:
        # Traverse left subtree
        while current:
            stack.append(current)
            current = current.left
        
        # Visit node
        current = stack.pop()
        if current.val <= prev_value:
            return False
        prev_value = current.val
        
        # Traverse right subtree
        current = current.right
    
    return True
```

#### Explanation

1. **Stack and Current Node**: Use a stack to manage the nodes and a pointer to traverse the tree.
    
2. **Left Subtree Traversal**: Traverse the left subtree until reaching the leftmost node.
    
3. **Visit Node**: Pop from the stack and check if the current node’s value is greater than the previous value.
    
4. **Right Subtree Traversal**: Move to the right subtree and repeat the process.
    

#### Pros and Cons

* **Pros**: Simple to implement and leverages the in-order property of BSTs.
    
* **Cons**: Requires additional space for the stack and is less intuitive than the recursive approach for some.
    

## Iterative Approach Using a Stack

The iterative approach uses a stack to manage the traversal, similar to the in-order traversal method but explicitly validates the BST properties at each step.

#### Code Implementation

```python
def is_valid_bst_iterative(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    stack = [(root, float('-inf'), float('inf'))]
    
    while stack:
        node, low, high = stack.pop()
        
        if not node:
            continue
        
        val = node.val
        if val <= low or val >= high:
            return False
        
        stack.append((node.right, val, high))
        stack.append((node.left, low, val))
    
    return True
```

#### Explanation

1. **Initial Check**: If the tree is empty, return true.
    
2. **Stack Management**: Use a stack to manage nodes and their valid ranges.
    
3. **Value Validation**: For each node, ensure its value is within the valid range.
    
4. **Subtree Validation**: Push the left and right children onto the stack with updated ranges.
    

## Comparing the Approaches

#### Recursive Approach

* **Time Complexity**: `O(n)`
    
* **Space Complexity**: `O(h)` (where `h` is the height of the tree)
    
* **Pros**: Clear and directly reflects the BST properties.
    
* **Cons**: Can run into recursion depth limits for very large trees.
    

#### In-Order Traversal Approach

* **Time Complexity**: `O(n)`
    
* **Space Complexity**: `O(n)` in the worst case (due to the stack)
    
* **Pros**: Simple to understand and implement.
    
* **Cons**: Requires additional space and is not as direct as the recursive approach.
    

#### Iterative Approach Using a Stack

* **Time Complexity**: `O(n)`
    
* **Space Complexity**: `O(h)`
    
* **Pros**: Avoids recursion depth issues and directly validates BST properties.
    
* **Cons**: Slightly more complex due to stack management.
    

## Conclusion

Validating a Binary Search Tree is an essential task for ensuring the correctness and efficiency of various applications. We explored three different methods to validate a BST using Python: the recursive approach, in-order traversal approach, and iterative approach using a stack. Each method has its own advantages and can be chosen based on the specific requirements of the application.

By understanding and implementing these methods, you can ensure that your BSTs maintain their crucial properties and support efficient operations.

### Related Articles

* "[Mastering Leetcode: Implementing a Trie (Prefix Tree) in Python](https://blog.seancoughlin.me/mastering-leetcode-implementing-a-trie-prefix-tree-in-python?source=more_series_bottom_blogs):
    
* "[Mastering Leetcode: Evaluating Reverse Polish Notation with Python](https://blog.seancoughlin.me/mastering-leetcode-evaluating-reverse-polish-notation-with-python)"
    
* "[Mastering the Clone Graph Problem on LeetCode: A Comprehensive Guide](https://blog.seancoughlin.me/mastering-the-clone-graph-problem-on-leetcode-a-comprehensive-guide)"