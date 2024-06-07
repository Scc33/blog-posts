---
title: "Mastering LeetCode: Implementing a Trie (Prefix Tree) in Python"
seoTitle: "Implementing Trie in Python: LeetCode Solution Guide"
seoDescription: "Learn how to implement a Trie (Prefix Tree) in Python with this comprehensive guide. Includes detailed explanations and code examples for LeetCode."
datePublished: Fri Jun 07 2024 19:56:33 GMT+0000 (Coordinated Universal Time)
cuid: clx53xg89000309judklgc94o
slug: mastering-leetcode-implementing-a-trie-prefix-tree-in-python
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1717790152134/0e134671-4e81-4ed6-bc55-1fd0d0f4ba8b.png
tags: interview, python, python3, leetcode, leetcode-solution

---

### Introduction to the Trie Data Structure

A trie, often pronounced as "try," is a versatile tree-like data structure that facilitates rapid retrieval of strings within a dataset. It's especially useful for applications such as autocomplete systems and spell-checking tools. Today, I'll take you through the process of implementing a trie, guided by [LeetCode's problem 208, "Implement Trie (Prefix Tree)."](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

Consider this scenario: You're tasked with designing a system that efficiently manages a large, dynamic collection of strings and supports fast lookup for complete words and prefixes. This is precisely where a trie comes into play.

> Implement the Trie class:
> 
> * `Trie()` Initializes the trie object.
>     
> * `void insert(String word)` Inserts the string `word` into the trie.
>     
> * `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false`otherwise.
>     
> * `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.
>     

### Considering Different Approaches to Implement a Trie

When planning to implement a trie, one might consider several methods:

1. **Array of Nodes:** Each node could potentially contain an array of 26 elements (for each letter of the English alphabet), pointing to subsequent nodes. However, this might lead to space inefficiency if many nodes have few children.
    
2. **Hash Map Based Nodes:** Alternatively, using a hash map to store children nodes keyed by characters can save space, as we only store active child nodes. This method combines space efficiency with relatively straightforward implementation logic, which is the approach I prefer and will elaborate on.
    
3. **Compressed Trie:** For applications requiring even more space efficiency, a compressed trie (or radix tree) minimizes space by combining chains of nodes with a single child into single nodes. This approach, however, complicates the implementation and might not be necessary for all use cases.
    

Each approach has its trade-offs in terms of space and time complexity, and the choice largely depends on the specific requirements of the application regarding memory usage and speed.

### Solution Description and Analysis

To solve the problem, the trie will be implemented using hash map based nodes. This approach efficiently handles the dynamic insertion and lookup of nodes without allocating unnecessary space. Here’s a step-by-step description:

* **Initialization (**`Trie()`): A root node is initialized, which acts as the starting point of the trie.
    
* **Inserting a Word (**`insert`): To insert a word, traverse from the root node, creating new nodes for each character if they do not exist.
    
* **Searching for a Word (**`search`): To search, traverse the trie. If at any point the character does not exist in the current node's children, return false. If the end of the word is reached, check if it's marked as a complete word.
    
* **Prefix Searching (**`startsWith`): Similar to the search function, but return true if you can traverse the trie up to the last character of the prefix.
    

The time complexity for insertion and search operations in the trie is O(L), where L is the length of the word or prefix being processed. This efficiency is due to the direct access capabilities of the hash map.

### Python Implementation of the Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
```

### Conclusion

Implementing a trie can dramatically increase the efficiency of operations that involve frequent searches for complete words and prefixes within a set of strings.

While there are several ways to implement this data structure, using hash map based nodes offers a balanced approach between space efficiency and ease of implementation.

By following the steps outlined above, one can effectively solve [LeetCode problem 208](https://leetcode.com/problems/implement-trie-prefix-tree/) and deepen their understanding of this fundamental data structure.