/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0; 

        int deep = 1; 
        stack<pair<TreeNode*, int>> depth; 
        depth.push(make_pair(root, 1)); 

        while (!depth.empty()) {
            pair<TreeNode*, int> temp = depth.top(); 
            depth.pop(); 
            deep = max(temp.second, deep); 

            if (temp.first->left) {
                depth.push(make_pair(temp.first->left, temp.second+1)); 
            } if (temp.first->right) {
                depth.push(make_pair(temp.first->right, temp.second+1)); 
            }
        }
        return deep; 
    }
};