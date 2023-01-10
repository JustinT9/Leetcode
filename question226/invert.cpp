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
// had trouble with a case where you had to handle the null nodes... 
// 30m... 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return root;    

        stack<TreeNode*> l; 
        stack<TreeNode*> r; 
        TreeNode* lPtr = root; 
        TreeNode* rPtr = root; 

        while (!l.empty() || !r.empty() || lPtr || rPtr) {
            while (lPtr || rPtr) {
                l.push(lPtr); 
                r.push(rPtr); 

                lPtr = lPtr->left; 
                rPtr = rPtr->right; 
            }
            lPtr = l.top(); 
            rPtr = r.top(); 
            l.pop(); 
            r.pop(); 
            if (lPtr && rPtr) {
                int temp = lPtr->val; 
                lPtr->val = rPtr->val; 
                rPtr->val = temp; 
            } else if (lPtr && !rPtr) {
                
            } 
            
            lPtr = lPtr->right; 
            rPtr = rPtr->left; 

        }
        return root; 
    }
};