// Solved in 50m  
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int start = 0; 
        int end = nums.size()-1; 
        TreeNode* root = NULL; 
        root = balancedTree(0, nums.size()-1, nums); 
        return root; 
    }

    TreeNode* balancedTree(int start, int end, vector<int>& nums) {    
        if (start > end) return NULL; 
        
        int middle = (start + end)/2; 
        TreeNode* n = new TreeNode(nums[middle]);
        n->left = balancedTree(start, middle-1, nums); 
        n->right = balancedTree(middle+1, end, nums); 
        return n; 
    }
}; 