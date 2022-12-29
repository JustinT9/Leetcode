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

// very close solution but there was a weird bug I could not find but the implementation and the idea of it was close as well 
// time: ~1h
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        TreeNode* first = root; 
        TreeNode* second = root; 
        stack<TreeNode*> data1; 
        stack<TreeNode*> data2; 

        while (first != second || (first && second)) {
            while (first && second) {
                data1.push(first); 
                data2.push(second); 

                // compare 
                if (first->val != second->val) return false; 

                first = first->left;
                second = second->right;  
            } 
            if (first && !second) return false;
            if (!first && second) return false;

            first = data1.top(); 
            second = data2.top(); 

            data1.pop(); 
            data2.pop(); 

            first = first->right; 
            second = second->left; 

            if (first == second) break; 
        }
        return true; 
    }
};