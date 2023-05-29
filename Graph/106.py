class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        inorder: left->root->right
        postorder: left->right->root
        root: postorder[-1]
        -> index of root in inorder
        inorder[:idx] -> left sub-tree
        inorder[idx:] -> right sub-tree
        left -> recursion called buildtree(inorder[:idx])
        right -> recursion called buildtree(inorder[idx:])
        [8 9 3 15 20 7]
        [8 9 15 7 20 3] 
        因為postorder的最後一個數是right sub-tree 的root,
        所以要先build right sub-tree
        """

        # O(n)
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            root_idx = inorderIdx[root.val]    #O(1)
            root.right = helper(root_idx+1, r)
            root.left = helper(l, root_idx-1)
            return root
        
        return helper(0, len(inorder) - 1)
        
        """
        # O(n^2)
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        root_idx = inorder.index(root.val)   # O(n)           
        root.right = self.buildTree(inorder[root_idx+1:], postorder)        
        root.left = self.buildTree(inorder[:root_idx], postorder)
        
        return root
        """
