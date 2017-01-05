
# Tree Traversal

[https://github.com/joowani/binarytree](https://github.com/joowani/binarytree)

```python
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```


```python
from binarytree import tree, pprint, Node

my_tree = tree(height=2, balanced=True)

pprint(my_tree)
```

    
        __6__    
       /     \   
      4       1  
     / \     / \ 
    5   3   0   2
                 


## In-Order Traversal


```python
def inOrderTraversal(n):
    if not n:
        return
    inOrderTraversal(n.left)
    print(n.value)
    inOrderTraversal(n.right)
    
    
inOrderTraversal(my_tree)
```

    5
    4
    3
    6
    0
    1
    2


## Pre-Order Traversal


```python
def preOrderTraversal(n):
    if not n:
        return
    print(n.value)
    preOrderTraversal(n.left)
    preOrderTraversal(n.right)
    
    
preOrderTraversal(my_tree)
```

    6
    4
    5
    3
    1
    0
    2


## Post-Order Traversal


```python
def postOrderTraversal(n):
    if not n:
        return
    postOrderTraversal(n.left)
    postOrderTraversal(n.right)
    print(n.value)

    
    
postOrderTraversal(my_tree)
```

    5
    3
    4
    0
    2
    1
    6


## Level-Order Traversal



```python
def levelOrderTraversal(n):
    q = []
    q.append(n)
    
    while q:
        node = q[0]
        q.append(node.left)
        q.append(node.right)
        q = q[1:]
        print(node.value)

    

levelOrderTraversal(my_tree)
```

    6
    4
    1
    5
    3
    0
    2


# Invert a Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            return self.solve(root)
        return root

    def solve(self, node):
        if not node:
            return node
        node.right, node.left = node.left, node.right
        self.solve(node.left)
        self.solve(node.right)
        return node
```