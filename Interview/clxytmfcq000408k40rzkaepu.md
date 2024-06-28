---
title: "Mastering the MinStack: Efficiently Supporting Minimum Element Retrieval in Constant Time"
seoTitle: "Efficient MinStack: Constant Time Min Element Retrieval"
seoDescription: "Learn how to implement a MinStack with constant time push, pop, top, and getMin operations in Python. Perfect for coding interviews!"
datePublished: Fri Jun 28 2024 15:01:08 GMT+0000 (Coordinated Universal Time)
cuid: clxytmfcq000408k40rzkaepu
slug: mastering-the-minstack-efficiently-supporting-minimum-element-retrieval-in-constant-time
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1719586564794/3c1da32f-9587-46d1-870e-fbafb2e92907.webp
tags: interview, python, data-structures, leetcode, leetcode-solution

---

## Introduction

Data structures are the backbone of efficient algorithms, providing the necessary foundation to solve complex problems swiftly and effectively. One intriguing challenge is designing a stack that supports not only the usual operations like push, pop, and top but also retrieving the minimum element in constant time.

This blog post delves into the [MinStack problem from Leetcode](https://leetcode.com/problems/min-stack/), exploring the problem, key considerations, and a robust Python implementation.

### Understanding the Problem

The MinStack problem requires creating a stack data structure that supports the following operations, all in constant O(1) time:

* `push(val)`: Pushes the element `val` onto the stack.
    
* `pop()`: Removes the element on the top of the stack.
    
* `top()`: Gets the top element of the stack.
    
* `getMin()`: Retrieves the minimum element in the stack.
    

> ##### Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
> 
> Implement the `MinStack` class:
> 
> * `MinStack()` initializes the stack object.
>     
> * `void push(int val)` pushes the element `val` onto the stack.
>     
> * `void pop()` removes the element on the top of the stack.
>     
> * `int top()` gets the top element of the stack.
>     
> * `int getMin()` retrieves the minimum element in the stack.
>     
> 
> You must implement a solution with `O(1)` time complexity for each function.
> 
> **Example 1:**
> 
> ```plaintext
> Input
> ["MinStack","push","push","push","getMin","pop","top","getMin"]
> [[],[-2],[0],[-3],[],[],[],[]]
> 
> Output
> [null,null,null,null,-3,null,0,-2]
> 
> Explanation
> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.getMin(); // return -3
> minStack.pop();
> minStack.top();    // return 0
> minStack.getMin(); // return -2
> ```

### Key Considerations

##### **Time Complexity**

Ensuring all operations execute in constant time is paramount. This means each function (`push`, `pop`, `top`, and `getMin`) should have a time complexity of `O(1)`.

##### **Space Complexity**

The solution must balance efficiency and space usage. Using additional data structures, like auxiliary stacks, can help achieve constant time complexity but may increase space complexity. Our approach uses two stacks: one to store all elements and another to store the minimum elements.

##### **Edge Cases**

Handling edge cases, such as operations on an empty stack or when multiple elements have the same minimum value, is crucial for a robust implementation.

## Solution Strategy

To achieve constant time complexity for all operations, we use two stacks:

* **Main Stack (**`stack`): Stores all the elements.
    
* **Minimum Stack (**`min_stack`): Stores the minimum elements at each stage.
    

### Algorithm Design

1. **Push Operation**: When pushing a value, it's added to the main stack. If the minimum stack is empty or the new value is less than or equal to the current minimum, it's also pushed onto the minimum stack.
    
2. **Pop Operation**: The value is popped from the main stack. If this value is the current minimum (top of the minimum stack), it's also popped from the minimum stack.
    
3. **Top Operation**: Returns the top element of the main stack.
    
4. **GetMin Operation**: Returns the top element of the minimum stack, which is the current minimum.
    

### Implementation in Python

Here’s the complete implementation of the MinStack class:

```python
class MinStack:
    def __init__(self):
        # Initialize two stacks: one for all elements and one for minimum elements
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # If the min_stack is empty or the new value is less than or equal to the current minimum, push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the main stack is not empty, pop the top value
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current minimum, pop it from the min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top value of the main stack if it is not empty
        if self.stack:
            return self.stack[-1]
        return -1  # or raise an exception

    def getMin(self) -> int:
        # Return the top value of the min_stack if it is not empty (the current minimum)
        if self.min_stack:
            return self.min_stack[-1]
        return -1  # or raise an exception
```

### Important Considerations

##### **Efficiency**

The implementation ensures all operations—`push`, `pop`, `top`, and `getMin`—are executed in O(1) time complexity, making it highly efficient for stack operations.

##### **Edge Case Handling**

* **Empty Stack**: The methods `top` and `getMin` handle cases where the stack is empty by returning a special value (`-1`) or raising an exception.
    
* **Duplicate Minimum Values**: The `min_stack` correctly handles duplicate minimum values. When a minimum value is popped, only the corresponding entry in the `min_stack` is removed.
    

##### **Correctness**

The use of two stacks ensures that the minimum value is always tracked accurately, maintaining the integrity of the stack operations.

#### **Testing the Implementation**

Testing is crucial to verify the correctness of the implementation. Here are some test cases to demonstrate the functionality:

```python
def test_min_stack():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3, "Test Case 1 Failed"
    minStack.pop()
    assert minStack.top() == 0, "Test Case 2 Failed"
    assert minStack.getMin() == -2, "Test Case 3 Failed"
    print("All test cases passed.")

test_min_stack()
```

##### **Expected Outcomes**

1. After pushing `-2`, `0`, and `-3` onto the stack, `getMin` should return `-3`.
    
2. After popping the top element (`-3`), `top` should return `0`.
    
3. After popping `-3`, `getMin` should return `-2`.
    

## Conclusion

Designing a MinStack that supports constant time operations for pushing, popping, retrieving the top element, and finding the minimum element is a fascinating exercise in efficient algorithm design. By leveraging two stacks, we can achieve the desired performance, ensuring that all operations are handled in `O(1)` time.

Implementing and testing this solution not only enhances understanding of stack data structures but also prepares one for tackling similar problems in coding interviews.

### Related Articles

Some related LeetCode medium articles:

* "[**Mastering LeetCode's Coin Change Problem: A Comprehensive Guide**](https://blog.seancoughlin.me/mastering-leetcodes-coin-change-problem-a-comprehensive-guide)**"**
    
* "[**Mastering LeetCode: Solving the "Product of Array Except Self" Problem**](https://blog.seancoughlin.me/mastering-leetcode-solving-the-product-of-array-except-self-problem?source=more_series_bottom_blogs)**"**
    
* "[**Mastering the Clone Graph Problem on LeetCode: A Comprehensive Guide**](https://blog.seancoughlin.me/mastering-the-clone-graph-problem-on-leetcode-a-comprehensive-guide?source=more_series_bottom_blogs)**"**
    
* "[**Mastering LeetCode: Converting Roman to Integer**](https://blog.seancoughlin.me/mastering-leetcode-converting-roman-to-integer?source=more_series_bottom_blogs)**"**