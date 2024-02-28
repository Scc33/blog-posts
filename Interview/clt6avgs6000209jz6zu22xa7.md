---
title: "Mastering LeetCode: Merge Two Sorted Lists"
seoTitle: "Efficient Solutions for Merging Two Sorted Lists: A Guide"
seoDescription: "Master the art of merging two sorted lists with this comprehensive guide. Explore tips, tricks, and best practices to ace this LeetCode challenge."
datePublished: Wed Feb 28 2024 21:19:55 GMT+0000 (Coordinated Universal Time)
cuid: clt6avgs6000209jz6zu22xa7
slug: mastering-leetcode-merge-two-sorted-lists
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1709155053181/697865a9-0df5-4e3b-b74b-ddd74351bf62.webp
tags: interview, java, python, typescript, interview-preparations

---

## Introduction

The problem of [merging two sorted linked (LeetCode 21)](https://leetcode.com/problems/merge-two-sorted-lists/description/) lists into a single sorted list is a classic algorithmic challenge often encountered in software engineering interviews. This task tests one's understanding of linked list data structures, pointer manipulation, and algorithm efficiency.

Imagine you're given two lists: `list1 = [1,2,4]` and `list2 = [1,3,4]`. Your goal is to merge these lists into one sorted list, resulting in `[1,1,2,3,4,4]`. This seemingly straightforward task can reveal deep insights into an engineer's problem-solving skills.

## Problem Solving Strategy

To tackle this problem:

1. We start with a dummy node to simplify edge cases and maintain a current pointer to build the new list.
    
2. We compare the values of nodes from both lists, appending the smaller one to the current node, and moving the pointer of the appended list forward. This process continues until we reach the end of one or both lists.
    
3. If one list is exhausted before the other, we link the remainder of the non-exhausted list to the end of the merged list. This ensures that all elements are included.
    

The time complexity of this algorithm is O(n + m), where n and m are the lengths of the two lists, as each element is visited exactly once.

The space complexity is O(1), as we only allocate a few pointers regardless of the input size.

## Python Solution

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point
        head = cur = ListNode(0)
        # Traverse both lists
        while list1 and list2:
            # Link the smaller value to 'cur' and advance
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # Attach any remaining elements
        cur.next = list1 or list2
        # Return the merged list, skipping the dummy node
        return head.next
```

## TypeScript Solution

```typescript
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let cur = new ListNode(0);
    const head = cur;
    while (list1 && list2) {
        if (list1.val < list2.val) {
            cur.next = list1;
            list1 = list1.next;
        } else {
            cur.next = list2;
            list2 = list2.next;
        }
        cur = cur.next;
    }
    cur.next = list1 || list2;
    return head.next;
}
```

## Java Solution

```java
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(0);
        ListNode cur = head;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                cur.next = list1;
                list1 = list1.next;
            } else {
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }
        cur.next = (list1 != null) ? list1 : list2;
        return head.next;
    }
}
```

### Conclusion

Merging two sorted lists is an essential problem that showcases the importance of understanding data structures and algorithmic strategies.

Remember, the key to excelling in coding interviews is practice, understanding the underlying principles, and adapting to various problem-solving scenarios.