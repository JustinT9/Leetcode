class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        // as you add to the hashmap keep on checking for the 
        // other indices of the target and if found then return 
        // the indexes otherwise keep on adding and this 
        // handles the cases for duplicates as well and makes 
        // code easier and concise 

        // mem: O(n) since worse case is allocating a hash map of size n 
        // time complex: O(n) since worse case you will have to traverse
        // through the array of size n 
        for (int i = 0; i < nums.size(); i++) {
            if (indices.find(target - nums[i]) != indices.end()) {
                return {indices[target - nums[i]], i};
            }
            indices[nums[i]] = i;
        }
        return {};
    }
};