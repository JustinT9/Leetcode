/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*, int> nodes; 

        while (head) {
            if (nodes[head] == 2) {
                return true;  
            }

            nodes[head]++; 
            head = head->next; 
        }
    
        return false; 
    }
};