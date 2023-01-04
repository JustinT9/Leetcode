/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// took around 30m
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int sizeA = 0; int sizeB = 0; 
        ListNode* ptrA = headA; ListNode* ptrB = headB; 

        while (ptrA) {
            sizeA++; 
            ptrA = ptrA->next; 
        } while (ptrB) {
            sizeB++; 
            ptrB = ptrB->next; 
        }

        ptrA = headA; ptrB = headB; 
        if (sizeA < sizeB) {
            for (int i = 0; i < sizeB-sizeA; i++) {
                ptrB = ptrB->next; 
            }
            for (int i = 0; i < sizeA; i++) {
                if (ptrA == ptrB) {
                    return ptrA; 
                }
                ptrA = ptrA->next; 
                ptrB = ptrB->next; 
            }
        } else {
            for (int i = 0; i < sizeA-sizeB; i++) {
                ptrA = ptrA->next; 
            }
            for (int i = 0; i < sizeB; i++) {
                if (ptrA == ptrB) {
                    return ptrA; 
                }
                ptrA = ptrA->next; 
                ptrB = ptrB->next; 
            }
        }
        return NULL; 
    }
};