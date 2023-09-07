---
title: "How to validate a Sudoku board"
seoTitle: "Validate Sudoku Board: Step-by-Step Guide"
datePublished: Thu Sep 07 2023 15:30:52 GMT+0000 (Coordinated Universal Time)
cuid: clm9bsdbx00030al6c6aa3nx6
slug: how-to-validate-a-sudoku-board
tags: algorithms, python, interview-questions, leetcode, big-o-notation

---

## The Problem

With this article, I will be covering the [valid sudoku Leetcode problem](https://leetcode.com/problems/valid-sudoku/).

Leetcode describes the problem with the following:

> Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:
> 
> 1. Each row must contain the digits `1-9` without repetition.
>     
> 2. Each column must contain the digits `1-9` without repetition.
>     
> 3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.
>     
> 
> **Note:**
> 
> * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
>     
> * Only the filled cells need to be validated according to the mentioned rules.
>     

Leetcode ranks this problem as a medium. I think that is an appropriate rating. The solution is feasible but does require some out-of-the-box reasoning.

## The Solution

```python
    def isValidSudoku(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != ".":
                    row = str(number) + "row" + str(i)
                    column = str(number) + "column" + str(j)
                    block = str(number) + "block" + str(i / 3) + "/" + str(j/3)
                    if row in seen or column in seen or block in seen:
                        return False
                    seen.add(row)
                    seen.add(column)
                    seen.add(block)
        return True
```

### Solution Description

1. `seen = set()`: Creates an empty set named `seen` to keep track of numbers that have already appeared in rows, columns, and 3x3 blocks.
    
2. Two nested loops `for i in range(9)` and `for j in range(9)` iterate through each cell of the 9x9 board.
    
3. `number = board[i][j]`: Stores the current cell's value in the variable `number`.
    
4. `if number != ".":`: Checks if the cell is not empty (a dot indicates an empty cell in this context).
    
5. `row = str(number) + "row" + str(i)`: Creates a string like `1row0` to indicate that the number 1 is in row 0.
    
6. `column = str(number) + "column" + str(j)`: Creates a string like `1column0` to indicate that the number 1 is in column 0.
    
7. `block = str(number) + "block" + str(i / 3) + "/" + str(j/3)`: Creates a string like `1block0/0` to indicate that the number 1 is in the top-left 3x3 block.
    
8. `if row in seen or column in seen or block in seen:`: Checks if any of these strings already exist in the `seen` set. If so, the board is not valid and the function returns `False`.
    
9. `seen.add(row)`, `seen.add(column)`, `seen.add(block)`: Adds the newly created strings to the `seen` set so that they can be checked against future cells.
    
10. If all cells are valid, the function returns `True`, indicating a valid Sudoku board.Big O Analysis
    

### Big O Analysis

Assuming `n` is the side length. We have a double for-loop so that is at least `O(n^2)`. Inside the nested loops, the operations (like adding to a set, creating strings, and checking for membership in a set) are `O(1)` operations. Therefore, the overall runtime is `O(n^2)`.