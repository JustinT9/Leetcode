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
//  took about 12m 
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return NULL; 
        
        ListNode* prev = NULL; 
        ListNode* curr = head; 
        ListNode* n = head->next; 

        while (curr) {
            curr->next = prev; 

            prev = curr; 
            curr = n; 
            if (n) n = n->next; 
        } head = prev; 
    return head; 
    }
};