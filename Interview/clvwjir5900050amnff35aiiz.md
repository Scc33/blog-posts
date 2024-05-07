---
title: "Mastering the Clone Graph Problem on LeetCode: A Comprehensive Guide"
seoTitle: "Clone Graph: Ace LeetCode with DFS & BFS"
seoDescription: "Explore detailed Python solutions for the Clone Graph problem on LeetCode, featuring both DFS and BFS approaches."
datePublished: Tue May 07 2024 15:23:23 GMT+0000 (Coordinated Universal Time)
cuid: clvwjir5900050amnff35aiiz
slug: mastering-the-clone-graph-problem-on-leetcode-a-comprehensive-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1715095287929/fd203bf3-dbc5-4f20-88bc-707ff34139ea.jpeg
tags: interview, python, graph, leetcode, leetcode-solution

---

## Introduction to the Clone Graph Problem

In graph theory, cloning or making a deep copy of a graph ([LeetCode 133 Clone Graph](https://leetcode.com/problems/clone-graph/description/)) is a fundamental challenge, especially in coding interviews where understanding data structures is crucial. The problem is typically presented with a node from a connected, undirected graph and requires you to return a deep copy of the entire graph. Each node in the graph has a unique integer value and a list of its neighbors.

> Given a reference of a node in a **connected** undirected graph.
> 
> Return a **deep copy** (clone) of the graph.
> 
> Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.
> 
> ```python
> class Node {
>     public int val;
>     public List<Node> neighbors;
> }
> ```
> 
> [![Example graph cloning](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png align="left")](https://leetcode.com/problems/clone-graph/description/)

---

## Exploring Different Approaches to Solve the Problem

When facing the Clone Graph challenge, two primary strategies emerge: using recursion and using a breadth-first search (BFS). Both methods involve traversing the graph and creating new nodes, but they differ significantly in their implementation:

1. **Recursive Depth-First Search (DFS)**: This approach leverages the call stack as an implicit stack, making it elegant and relatively straightforward. It involves visiting each node, creating a copy, and recursively doing the same for each unvisited neighbor.
    
2. **Breadth-First Search (BFS)**: In contrast to recursion, BFS uses an explicit queue to manage the traversal. This method is particularly useful in avoiding stack overflow errors in large graphs and provides a systematic way to clone node by node.
    

### Solving the Problem in Python: Recursive Approach

Let's dive into the recursive solution for the Clone Graph problem. The Python code below utilizes a helper function that employs recursion to traverse and clone the graph:

```python
class Solution:
    def helper(self, node, visited):
        if node is None:
            return None

        # Create a new node for the given node's value
        new_node = Node(node.val)
        visited[node.val] = new_node  # Mark this node as visited

        # Recursively clone the neighbors
        for adj_node in node.neighbors:
            if adj_node.val not in visited:
                new_node.neighbors.append(self.helper(adj_node, visited))
            else:
                new_node.neighbors.append(visited[adj_node.val])

        return new_node
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.helper(node, {})
```

This recursive method is efficient with a time complexity of O(n), where n is the number of nodes in the graph, since each node is visited exactly once. The space complexity is also O(n), primarily due to the recursion stack and the space needed for the `visited` dictionary.

### Solving the Problem in Python: BFS Approach

For those who prefer non-recursive methods, here is how you can implement a BFS solution to clone a graph:

```python
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        clones = {node.val: Node(node.val, [])}

        while queue:
            cur_node = queue.popleft()
            cur_clone = clones[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                
                cur_clone.neighbors.append(clones[neighbor.val])
                
        return clones[node.val]
```

This BFS approach also maintains an O(n) time complexity, with the space complexity primarily due to the queue and the dictionary storing cloned nodes.

## Conclusion

Understanding different methods to solve the Clone Graph problem provides a robust foundation for tackling similar problems in coding interviews.

Whether you prefer the elegance of recursion or the control of BFS, mastering these techniques will enhance your problem-solving skills and prepare you for complex challenges in software engineering interviews.