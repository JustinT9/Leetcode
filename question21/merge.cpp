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
// took around 20 minutes 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = NULL; 
        ListNode* ptr = NULL; 

        if (!list1 && !list2) return head; 
        else if (!list1 && list2) return list2; 
        else if (list1 && !list2) return list1; 

        if (list1->val >= list2->val) {
            ptr = head = list2; 
            list2 = list2->next; 
        } else if (list1->val <= list2->val) {
            ptr = head = list1; 
            list1 = list1->next; 
        }

        while (list1 && list2) {
            if (list1->val >= list2->val) {
                ptr->next = list2; 
                list2 = list2->next; 
                ptr = ptr->next; 
            } else if (list1->val <= list2->val) {
                ptr->next = list1; 
                list1 = list1->next; 
                ptr = ptr->next; 
            }
        } 

        if (list1) {
            ptr->next = list1; 
        } else if (list2) {
            ptr->next = list2; 
        }

        return head; 
    }
};