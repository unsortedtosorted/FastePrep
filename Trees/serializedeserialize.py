# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.r = ""
        if not root:
            return self.r
        def dfs(root):
            
            if root:
                
                if not self.r:
                    
                    self.r = str(root.val)
                else:
                    self.r += " "+str(root.val)
                dfs(root.left)
                dfs(root.right)
            else:
                self.r+=" $"
                
        dfs(root)
        return self.r
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(" ")

        
        
        def preorder(ind):
            
            if ind < len(data):
                
                if data[ind] == '$':
                    return None,ind+1
                
                else:
                    
                    root = TreeNode(data[ind])
                    root.left,rind = preorder(ind+1)
                    root.right,nex = preorder(rind)
                    return root,nex
        
        
        return preorder(0)[0]
