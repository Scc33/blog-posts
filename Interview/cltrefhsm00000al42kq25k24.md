---
title: "Mastering LeetCode's 'Reverse Linked List': A Comprehensive Guide for Engineers"
seoTitle: "Reverse a Linked List: Iterative & Recursive Tips"
seoDescription: "Master reversing a linked list for coding interviews with a guide on iterative and recursive strategies. Boost your problem-solving skills now."
datePublished: Thu Mar 14 2024 15:42:38 GMT+0000 (Coordinated Universal Time)
cuid: cltrefhsm00000al42kq25k24
slug: mastering-leetcodes-reverse-linked-list-a-comprehensive-guide-for-engineers
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1710430935321/a0200e27-6e27-4ff2-996a-9c5fab4a5698.webp
tags: interview, python, linked-list, leetcode, leetcode-solution

---

Welcome to this tutorial on solving a classic problem that often appears in software engineering interviews: reversing a singly linked list. This challenge, commonly found on [LeetCode (LeetCode 206)](https://leetcode.com/problems/reverse-linked-list/description/), is a fantastic way to understand essential concepts in data structures and algorithms.

Whether you're new to engineering interviews or an experienced engineer brushing up on your skills, this guide aims to equip you with the knowledge to confidently tackle linked list problems.

## Introduction to the Problem

The problem statement is straightforward: given the head of a singly linked list, reverse the list, and return the head of the reversed list. For instance:

* Input: `head = [1,2,3,4,5]`, Output: `[5,4,3,2,1]`
    
    [![Regular reversal example](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg align="center")](https://leetcode.com/problems/reverse-linked-list/description/)
    
    Input: `head = [1,2]`, Output: `[2,1]`
    
    [![Base case reversal example](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg align="center")](https://leetcode.com/problems/reverse-linked-list/description/)
    
    Input: `head = []`, Output: `[]`
    

## Understanding the Solution

To reverse a linked list, we can use the [two-pointer technique](https://www.geeksforgeeks.org/two-pointers-technique/), a common strategy for linked list problems. This involves using two pointers, typically named `prev` and `current`, to traverse the list and reverse the links between nodes.

### Big O Notation Analysis

* **Time Complexity:** O(n), where n is the number of nodes in the linked list. We need to traverse all nodes once.
    
* **Space Complexity:** O(1) for the iterative approach, as we only use a fixed amount of extra space. For the recursive approach, it's O(n) due to the call stack.
    

### Recursive Solution in Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    # Base case: if list is empty or has only one element
    if not head or not head.next:
        return head
    # Reverse the rest of the list
    new_head = self.reverseList(head.next)
    # Set the next of the next node to the current node to reverse
    head.next.next = head
    head.next = None  # Set the next of the current node to None
    return new_head  # Return the new head of the reversed list
```

### Iterative Solution in Python

```python
def reverseList(self, head: ListNode) -> ListNode:
    prev, cur = None, head
    while cur:
        temp = cur.next  # Store the next node
        cur.next = prev  # Reverse the current node's pointer
        prev = cur  # Move prev to current
        cur = temp  # Move to the next node
    return prev  # Prev will be the new head
```

### Recursion vs. Iteration: A Comparison

| Aspect | Recursion | Iteration |
| --- | --- | --- |
| **Space Complexity** | O(n) due to recursive call stack | O(1), only a few pointers used |
| **Ease of Understanding** | Might be less intuitive at first | Generally more intuitive |
| **Performance** | Can lead to stack overflow in languages with limited stack size | More consistent performance |
| **Use Case** | Elegant solution for smaller lists or when space complexity is not an issue | Preferred for large lists or when maintaining a minimal space footprint is crucial |

## Solution in TypeScript

```typescript
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let cur: ListNode | null = head;
    while (cur !== null) {
        let temp: ListNode | null = cur.next;  // Store next node
        cur.next = prev;  // Reverse the link
        prev = cur;  // Move prev forward
        cur = temp;  // Move cur forward
    }
    return prev;  // New head of the reversed list
}
```

## Solution in Java

```java
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode

 next) { this.val = val; this.next = next; }
}

public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode cur = head;
    while (cur != null) {
        ListNode temp = cur.next;  // Store next node
        cur.next = prev;  // Reverse the link
        prev = cur;  // Move prev forward
        cur = temp;  // Move cur forward
    }
    return prev;  // New head of the reversed list
}
```

## Conclusion

Reversing a linked list is a fundamental problem that tests your understanding of linked lists and pointer manipulation. By mastering both iterative and recursive approaches, you'll be well-prepared for software engineering interviews.

Remember, practice is key to becoming proficient in these concepts. I hope this guide helps you on your journey to becoming a more confident and skilled software engineer.

Thank you for taking the time to read this post. Your dedication to learning and improving is what makes the journey of programming so rewarding. Happy coding!