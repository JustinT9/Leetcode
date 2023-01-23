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
// time: 35m 
// had trouble with the conditions 
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int lMax = 0; int rMax = 0; int prev = 0; 
        stack<pair<TreeNode*, int>> lNodes; 
        stack<pair<TreeNode*, int>> rNodes;
        lNodes.push(make_pair(root->left, 0)); 
        rNodes.push(make_pair(root->right, 0)); 

        while (prev != (lNodes.size() + rNodes.size())) {
            prev = lNodes.size() + rNodes.size(); 
            if (lNodes.top().first->right) {
                lNodes.push(make_pair(lNodes.top().first->right, lNodes.top().second++)); 
                lMax = max(lMax, lNodes.top().second); 
            } if (lNodes.top().first->left) {
                lNodes.push(make_pair(lNodes.top().first->left, lNodes.top().second++)); 
                lMax = max(lMax, lNodes.top().second); 
            } if (rNodes.top().first && rNodes.top().first->left) {
                rNodes.push(make_pair(rNodes.top().first->left, rNodes.top().second++)); 
                rMax = max(lMax, rNodes.top().second); 
            } if (rNodes.top().first && rNodes.top().first->right) {
                rNodes.push(make_pair(rNodes.top().first->right, rNodes.top().second++)); 
                rMax = max(lMax, rNodes.top().second); 
            }
        } 
        return rMax + lMax; 
    }
};