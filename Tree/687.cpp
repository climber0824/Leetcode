class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        
        return ans;
        
    }
    int dfs(TreeNode* root, int& ans) {
        if (!root) return 0;
        int left_children = root->left ? dfs(root->left, ans) : 0;
        int right_children = root->right ? dfs(root->right, ans) : 0;
        int left = root->left && root->left->val == root->val ?left_children + 1 : 0;
        int right = root->right && root->right->val == root->val ? right_children + 1 : 0;
        ans = max(ans, left+right);
        return max(left, right);

    }
};
