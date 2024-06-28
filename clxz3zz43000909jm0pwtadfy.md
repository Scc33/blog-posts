---
title: "Mastering LeetCode: Counting the Number of Islands in a 2D Binary Grid"
seoTitle: "Efficiently Count Islands in a 2D Grid with DFS"
seoDescription: "Learn how to solve the Leetcode island counting problem using DFS. Step-by-step guide with Python code and detailed explanations."
datePublished: Fri Jun 28 2024 19:51:36 GMT+0000 (Coordinated Universal Time)
cuid: clxz3zz43000909jm0pwtadfy
slug: mastering-leetcode-counting-the-number-of-islands-in-a-2d-binary-grid
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1719603847752/2e3357c0-b68f-4bfc-9f7c-99f6170707e2.webp
tags: interview, algorithms, python, graph, leetcode

---

## Introduction

Counting the number of islands in a 2D binary grid is a classic problem that appears frequently in coding interviews ([LeetCode 200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)). This problem challenges you to identify and count distinct islands in a grid where '1' represents land and '0' represents water. Solving this problem not only helps you practic[e depth-first search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search) algorithms but also enhances your problem-solving skills for tackling similar graph traversal problems.

In this article, we will delve into the problem statement, explore the DFS approach to solve it, and provide a step-by-step guide with a complete Python implementation.

### Problem Statement

Here is the exact problem description from LeetCode:

> Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.
> 
> An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
> 
> **Example 1:**
> 
> ```plaintext
> Input: grid = [
>   ["1","1","1","1","0"],
>   ["1","1","0","1","0"],
>   ["1","1","0","0","0"],
>   ["0","0","0","0","0"]
> ]
> Output: 1
> ```
> 
> **Example 2:**
> 
> ```plaintext
> Input: grid = [
>   ["1","1","0","0","0"],
>   ["1","1","0","0","0"],
>   ["0","0","1","0","0"],
>   ["0","0","0","1","1"]
> ]
> Output: 3
> ```

## Solution Overview

To solve this problem, we will use the Depth-First Search (DFS) algorithm. DFS is a graph traversal technique that explores as far as possible along each branch before backtracking.

By using DFS, we can explore and mark all connected land cells starting from any unvisited land cell, effectively identifying and counting distinct islands.

### Step-by-Step Solution

#### Initial Setup

First, we initialize necessary variables:

* `rows` and `cols` to store the dimensions of the grid.
    
* A set `visited` to keep track of visited cells to avoid redundant work.
    

#### Depth-First Search (DFS) Function

The DFS function will:

* Take the current cell coordinates (`r`, `c`) as parameters.
    
* Check boundary conditions and whether the cell is water or already visited.
    
* Mark the cell as visited.
    
* Recursively explore all four possible directions (up, down, left, right) to visit all connected land cells.
    

#### Main Loop to Count Islands

We iterate through each cell in the grid. For each unvisited land cell, we initiate a DFS to explore the entire island and increment our island count.

### Complete Code Implementation

Here is the complete Python code with detailed comments for clarity:

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r: int, c: int):
            # Boundary check and check if the cell is water or already visited
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == '0' or 
                (r, c) in visited):
                return
            
            # Mark the cell as visited
            visited.add((r, c))
            
            # Explore all four possible directions (up, down, left, right)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        islands = 0
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land and not yet visited, it's a new island
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    # Perform DFS to mark all cells in this island as visited
                    dfs(r, c)
        
        return islands

# Example usage
solution = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid))  # Output: 3
```

### Optimizations and Improvements

While the DFS approach is straightforward and effective, there are potential optimizations for large grids:

* **Iterative DFS**: Using an explicit stack instead of recursion to avoid potential stack overflow in deep recursion.
    
* **Breadth-First Search (BFS)**: An alternative approach that uses a queue to explore the grid level by level.
    
* **Union-Find**: A more advanced technique that uses a disjoint set data structure to group and count connected components efficiently.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1719604268650/c609a150-abcc-4c18-bd1f-f73ff909ba37.webp align="center")

## Conclusion

In this article, we explored how to solve the Leetcode problem of counting the number of islands in a 2D binary grid using the Depth-First Search (DFS) algorithm. By breaking down the problem and providing a detailed step-by-step solution, we demonstrated how DFS can effectively traverse and mark connected components in a grid.

Mastering such problems is crucial for coding interviews, and practicing similar challenges will enhance your problem-solving skills and algorithmic thinking.

Happy coding!

### Related Articles

* "[**Mastering the 01 Matrix Problem on LeetCode: A Detailed Guide for Aspiring Software Engineers**](https://blog.seancoughlin.me/mastering-the-01-matrix-problem-on-leetcode-a-detailed-guide-for-aspiring-software-engineers)**"**
    
* "[**Mastering Binary Tree Level Order Traversal for LeetCode Interviews**](https://blog.seancoughlin.me/mastering-binary-tree-level-order-traversal-for-leetcode-interviews)**"**
    
* "[**Mastering the Staircase: Dynamic Programming Solutions for LeetCode's Climbing Stairs Problem**](https://blog.seancoughlin.me/mastering-the-staircase-dynamic-programming-solutions-for-leetcodes-climbing-stairs-problem)**"**