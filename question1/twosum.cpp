// revised two sum solution issue was handling the duplicates and it did not work for some reason for the weird bugs...? 
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret; 
        unordered_map<int, vector<int>> numbers; 

        if (nums.size() == 2) return {0, 1}; 

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < target) {
                if (numbers.find(nums[i]) == numbers.end()) {
                    vector<int> temp = {i};
                    numbers.insert(make_pair(nums[i], temp)); 
                } else {
                    numbers[nums[i]].push_back(i); 
                }
            }
        }   

        if (target == 0) {
            ret.push_back(numbers.find(target)->second[0]); 
            ret.push_back(numbers.find(target)->second[1]); 
            return ret; 
        }

        for (unordered_map<int, vector<int>>::iterator itr = numbers.begin(); 
            itr != numbers.end(); itr++) {
            int remainder = target - itr->first; 
            if (numbers.find(remainder) == numbers.end()) continue;  

            if (itr->first != remainder) {
                ret.push_back(itr->second[0]); 
                ret.push_back(numbers.find(remainder)->second[0]);
                break;
            } else {
                ret.push_back(itr->second[0]); 
                ret.push_back(itr->second[1]); 
                break;
            }
        }

        return ret; 
    }
};