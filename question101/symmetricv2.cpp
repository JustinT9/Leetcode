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
        stack<TreeNode*> l;
        stack<TreeNode*> r; 
        TreeNode* lPtr = root;
        TreeNode* rPtr = root; 

        while (!r.empty() || !l.empty() || lPtr || rPtr) {
            // incorrect logic here 
            if (!lPtr || rPtr) return false;
            else if (lPtr || !rPtr) return false;
            
            while (lPtr || rPtr) {
                if (lPtr->val != rPtr->val) return false;   
                
                l.push(lPtr); r.push(rPtr); 

                lPtr = lPtr->left; 
                rPtr = rPtr->right; 
            }

            lPtr = l.top(); 
            rPtr = r.top(); 
            l.pop(); r.pop();
            lPtr = lPtr->right; 
            rPtr = rPtr->left; 
        }  
        return true; 
    }
};