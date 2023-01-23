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
    bool isSymmetric(TreeNode* root) {
        TreeNode* lPtr = root; TreeNode* rPtr = root; 
        stack<TreeNode*> lNodes = {}; 
        stack<TreeNode*> rNodes = {}; 

        while (!lNodes.empty() || !rNodes.empty() || lPtr || rPtr) {
            if ((lPtr && !rPtr) || (!lPtr && rPtr)) return false;

            while (lPtr && rPtr) {
                if (lPtr->val != rPtr->val) return false; 

                lNodes.push(lPtr); 
                rNodes.push(rPtr); 

                lPtr = lPtr->left; 
                rPtr = rPtr->right; 
            }

            lPtr = lNodes.top(); 
            rPtr = rNodes.top(); 
            lNodes.pop(); 
            rNodes.pop(); 
            lPtr = lPtr->right; 
            rPtr = rPtr->left; 
        }
        return true; 
    }
};