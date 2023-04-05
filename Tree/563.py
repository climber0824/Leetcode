class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.ans += abs(left - right)
            return node.val + left + right
        
        dfs(root)

        return self.ans
