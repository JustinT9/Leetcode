# python solution is more elegant and simpler and more intuitive 
# this is a recursive solution 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            self.invertTree( root.left )
            self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None

# DFS
def invertTree(self, root):
    stack = [root]
    # while the stack has something in it 
    while stack:
        # set it to the last element 
        node = stack.pop()
        # if valid and not none then swap 
        if node:
            node.left, node.right = node.right, node.left
            # extend it 
            stack.extend([node.right, node.left])
    return root