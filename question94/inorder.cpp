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
#include <stack>
#include <vector>


// took an hour 
// the issue was that I was not well versed on this topic when I cannot do it recursively
// based on the parameters and I tried doing it iteratively with a stack which was the right idea
// but I need to brush myself up on this topic 

// i could not easy pass the base cases since my code had many errors 
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret; 
        stack<TreeNode*> history; 

        if (root) history.push(root); 
        while (!history.empty()) {
            // traverse down the left path 
            while (root->left) {
                root = root->left; 
                history.push(root); 
            } 
            
            if (root) {
                ret.push_back(history.top()->val); 
                history.pop(); 
                ret.push_back(history.top()->val); 
                root = history.top();
                root = root->right; 
                history.push(root); 
                ret.push_back(history.top()->val); 

                while (root->val >= history.top()->val) {
                    history.pop(); 
                } 
            }
            ret.push_back(history.top()->val); 
            root = history.top()->right;
            history.push(root); 
        } 
        return ret; 
    }
};