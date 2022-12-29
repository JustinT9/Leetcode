// both the recursive and iterative solutions use O(n) time 
// complexity because it goes through all the nodes 
// and O(n) space complexity because it uses a stack--the call stack for recursion  
// of n nodes to store the data 

class Solution {
public:
    // the iterative solution using a stack 
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        stack<TreeNode*> todo;
        // condition where the traversal ends until the stack 
        // is empty or if there is a root at all 

        // because there are going to be cases when there 
        // is still none in the stack but there are still nodes 
        // you need to explore 
        while (root || !todo.empty()) {
            // go to the left most node 
            while (root) {
                todo.push(root);
                root = root -> left;
            }
            // have the node return to a valid node and not be null 
            root = todo.top();
            // pop it from the stack 
            todo.pop();
            // push back to vector 
            nodes.push_back(root -> val);
            // go to the right if possible and this 
            // important when looping back becuase of its relationship with 
            // the initial while loop and the root = top statement 
            root = root -> right;
        }
        return nodes;
    }
};

// the more intuitive solution when there is recursion being used 
// where there must be a driver function so a vector can be passed by reference 
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        inorder(root, nodes);
        return nodes;
    }
private:
    void inorder(TreeNode* root, vector<int>& nodes) {
        // base case if root leaf 
        if (!root) {
            return;
        }
        inorder(root -> left, nodes);
        nodes.push_back(root -> val);
        inorder(root -> right, nodes);
    }
};

// morris traversal solution with the best space complexity of O(1) while 
// O(N) time complexity 
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        while (root) {
            if (root -> left) {
                TreeNode* pre = root -> left;
                while (pre -> right && pre -> right != root) {
                    pre = pre -> right;
                }
                if (!pre -> right) {
                    pre -> right = root;
                    root = root -> left;
                } else {
                    pre -> right = NULL;
                    nodes.push_back(root -> val);
                    root = root -> right;
                }
            } else {
                nodes.push_back(root -> val);
                root = root -> right;
            }
        }
        return nodes;
    }
};