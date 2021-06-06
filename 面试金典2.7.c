#include <stdlib.h>

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    struct ListNode *pA = headA;
    struct ListNode *pB = headB;

    if (headA == NULL || headB == NULL)
        return NULL;
    while (pA != pB)
    {
        pA = pA == NULL ? headB : pA->next;
        pB = pB == NULL ? headA : pB->next;
    }
    return pA;
}