# Tree Traversals
# This programs displays the different types of Tree Traversals
# Pre-Order, Post-Order, In-Order, and Level-Order
# Yzer De Gula

from typing import Optional, List
from collections import deque

# Create our TreeNode Class
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Traversal:
    def printPreOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If there is no tree, return an empty list
        if not root:
            return []
        
        # Declare our result list
        result = []
        
        # Pre-Order goes Root, Left Subtree, then Right Subtree
        result.append(root.val)
        result.extend(self.printPreOrder(root.left))
        result.extend(self.printPreOrder(root.right))

        # Return result list
        return result
    

    def printPostOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If there is no tree, return an empty list
        if not root:
            return []
        
        # Declare our result list
        result = []

        # Post-Order goes Left Subtree, Right Subtree, then Root
        result.extend(self.printPostOrder(root.left))
        result.extend(self.printPostOrder(root.right))
        result.append(root.val)

        # Return result list
        return result
    

    def printInOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If there is no tree, return an empty list
        if not root:
            return []
        
        # Declare our result list
        result = []

        # In-Order goes Left Subtree, Root, then Right Subtree
        result.extend(self.printInOrder(root.left))
        result.append(root.val)
        result.extend(self.printInOrder(root.right))

        # Return result list
        return result

    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If there is no tree, return an empty list
        if not root:
            return []
        
        # Declare our result list
        result = []

        # If the root exists, Declare and put the root in the dequeue
        queue = deque([root])

        # While there is something in our queue
        while queue:
            # Remove the first node from the queue
            node = queue.popleft()

            # Append the node value to the result list
            result.append(node.val)

            # If a left child exists
            if node.left:
                # Add left child to queue
                queue.append(node.left)

            # If a right child exists
            if node.right:
                # Add right child to the queue
                queue.append(node.right)
            
        # Return result list
        return result

    
# Testing
traversal = Traversal()

node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(2,node1,node2)
node4 = TreeNode(3)
tree1 = TreeNode(1,node3,node4)

print("\nBelow Are The Different Types of Tree Traversals: ")

# Expects [1,2,4,5,3]
print("Pre-Order Traversal:   ", traversal.printPreOrder(tree1))

# Expects [4,5,2,3,1]
print("Post-Order Traversal:  ", traversal.printPostOrder(tree1))

# Expects [4,2,5,1,3]
print("In-Order Traversal:    ", traversal.printInOrder(tree1))

# Expects [1,2,3,4,5]
print("Level-Order Traversal: ", traversal.printLevelOrder(tree1))

print("\n")

        

        
        


