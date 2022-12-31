int maxDepth(TreeNode* root) {
    if (root == NULL) return 0;
    // pair to keep track of the max  
    stack<pair<TreeNode*, int>> s;
    // root has depth of 1 
    s.push({root, 1});
    // to compare and find the new max 
    int len = 1;
    // while there is stuff in the stack 
    while (!s.empty()) {
        // front is top of the stack 
        pair<TreeNode*, int> front = s.top(); 
        // pop the top of the stack 
        s.pop();
        // using max function to find the new max 
        len = max(len, front.second);

        // if there exists a left and right node push it to the stack and increment the depth 
        if (front.first->left) s.push({front.first->left, front.second+1});
        if (front.first->right) s.push({front.first->right, front.second+1});
    }
    return len;
}