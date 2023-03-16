class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:       
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)
        """
        thats bcuz of postorder is left-right-parent and inorder is left-parent-right. hence when we pop from postorder list we keep getting the right subtree's parent first. try out a simple example keeping this in mind it'll will get clear
        """
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)
        
        return root
