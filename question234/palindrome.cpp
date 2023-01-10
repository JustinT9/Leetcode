/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// had trouble with the odd cases
// 34m 
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head->next) return true; 

        stack<int> data; 
        while (head) {
            if (!data.empty()) {
                if (data.top() != head->val) {
                    data.push(head->val); 
                } else {
                    data.pop(); 
                }
            }
            head = head->next; 
        }
        if ((data.empty()) || ((data.size() != 1) && (data.size() % 2 != 0))) return true; 
        return false; 
    }
};