# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# done in 19 minutes and its way easier to do in python as well as doing it in bfs than dfs 
class Solution(object):
    def invertTree(self, root):
        queue = [root]
        while (len(queue) != 0):
            if queue[0] is not None: 
                queue[0].left, queue[0].right = queue[0].right, queue[0].left
            
                if (queue[0].left is not None):
                    queue.append(queue[0].left)
                if (queue[0].right is not None): 
                    queue.append(queue[0].right)

            queue.pop(0)
        return root 