class Solution {
public:
    int res = 0;
    int findTilt(TreeNode* root) {
        dfs(root);
        return res;
    }

    int dfs(TreeNode* root) {
        if (!root) return 0;
        int left = dfs(root->left);
        int right = dfs(root->right);
        res = res + abs(left - right);

        return root->val + left + right;
    }

};
