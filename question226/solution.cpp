// recursive method 
TreeNode* invertTree(TreeNode* root) {
    if (root) {
        invertTree(root->left);
        invertTree(root->right);
        std::swap(root->left, root->right);
    }
    return root;
}

// iterative method 
TreeNode* invertTree(TreeNode* root) {
    // uses one stack 
    std::stack<TreeNode*> stk;
    stk.push(root);
    
    // while stack is not empty 
    while (!stk.empty()) {
        // set node value to the top of the stack 
        TreeNode* p = stk.top();
        // pop it 
        stk.pop();
        // then push it and swap it 
        if (p) {
            stk.push(p->left);
            stk.push(p->right);
            // can swap it 
            std::swap(p->left, p->right);
        }
    }
    return root;
}