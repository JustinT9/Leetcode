// recursive DFS inorder traversal 
class Solution {
public:
    // driver function 
    bool isSymmetric(TreeNode* root) {
        // Tree is empty then it is already symmetric 
        if(root==NULL) return true; 
        // recursive function to go thorugh all of the nodes 
        return isSymmetricTest(root->left,root->right);
    }
    
    bool isSymmetricTest(TreeNode* p , TreeNode* q) {
        // left & right node is NULL 
        if (p == NULL && q == NULL) 
            return true; 

        //one of them is Not NULL
        else if (p == NULL || q == NULL) 
            return false; 
        
        // if the values are not matched 
        else if (p->val != q->val) 
            return false;
        
        // comparing left subtree's left child with right subtree's right child --AND-- 
        // comparing left subtree's right child with right subtree's left child
        return isSymmetricTest(p->left,q->right) && isSymmetricTest(p->right,q->left); 
    }
};

// iterative DFS 
bool isSymmetric(TreeNode* root) {
    // if empty then it is symmetric 
    if (!root) return true;
    // two stacks for the left and right side 
    stack<TreeNode*> sl, sr;

    // initialization 
    sl.push(root);
    sr.push(root);
    TreeNode * lp = root->left, *rp = root->right;

    //while the stacks are not empty or the pointers are not null 
    while (lp || ! sl.empty() || rp || !sl.empty()) {
        // if one is null and the other is not return false 
        if ((!lp && rp) || (lp && !rp)) return false;

        // if they are not null then 
        if (lp && rp){
            // if the values are not the same then false 
            if (lp->val != rp->val) return false;
            sl.push(lp);
            sr.push(rp);
            // where to go 
            lp = lp->left;
            rp = rp->right;
        // if they are both null then make it point to the next nodes 
        } else{
            lp = sl.top()->right;
            rp = sr.top()->left;
            sl.pop();
            sr.pop();
        }
    }
    return true;
}

// bfs algorithm--level order 
bool isSymmetric(TreeNode* root) {
    if (!root) return true;
    // a queue of pairs of nodes 
    queue<nodepair> q;
    // to compare the two mirrored nodes to see if they are the same 
    q.push(make_pair(root->left, root->right));
    // while the queue is not empty 
    while (!q.empty()){
        // visit the first pair 
        nodepair p = q.front();
        // pop it 
        q.pop();
        // the checks where if they are NULL then skip 
        if(!p.first && !p.second) continue;

        // otherwise if one of the nodes are NULL then it is invalid 
        if(!p.first || !p.second) return false;
        if(p.first->val != p.second->val) return false;

        // and then we go down another level 
        q.push(make_pair(p.first->left, p.second->right));
        q.push(make_pair(p.first->right, p.second->left));
    }
    return true;
}