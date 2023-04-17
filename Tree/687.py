class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return

            left = dfs(node.left)
            right = dfs(node.right)

            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0
            self.ans = max(self.ans, left + right)

            return max(left, right)

        dfs(root)

        return self.ans
