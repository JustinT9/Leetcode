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

// took 1h 10m 
// issue was that I could not figure out the counting logic behind it 
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int max = 0; 
        int calc = 0; 
        stack<TreeNode*> data; 
        
        while (!data.empty() || root) {
            if (root) {
                data.push(root); 
                root = root->left; 
                calc++; 
            } else {
                if (calc > max) {
                    max = calc; 
                }

                data.pop(); 
                calc--;  
                root = data.top()->right;  
            }
        }
        return max;
    }
};