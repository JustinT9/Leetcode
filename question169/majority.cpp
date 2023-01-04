class Solution {
public:
    // took around 20m 
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> numbers; 
        int num = 0; int max = 0; 

        for (int i = 0; i < nums.size(); i++) {
            if (numbers.find(nums[i]) == numbers.end()) {
                numbers.insert(make_pair(nums[i], 1)); 
            } else {
                numbers[nums[i]]++; 
            }

            if (numbers[nums[i]] > max) {
                num = nums[i]; 
                max = numbers[nums[i]]; 
            }
        }
        return num; 
    }
};