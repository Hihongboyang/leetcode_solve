#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};
// Common method, using an additional reverse sequence linked
bool isPalindrome(struct ListNode *head)
{
    if (head == NULL)
    {
        return true;
    }
    struct ListNode *new_head, *new_element = malloc(sizeof(struct ListNode)), *p_head=head;
    new_element->val = p_head->val;
    new_element->next = NULL;
    new_head = new_element;
    p_head = p_head->next;

    while (p_head != NULL)
    {
        struct ListNode *temp = malloc(sizeof(struct ListNode));
        temp->val = p_head->val;
        temp->next = new_head;
        new_head = temp;
        p_head = p_head->next;
    }

    while (head != NULL && new_head != NULL)
    {
        if (head->val != new_head->val)
        {
            return false;
        }
        head = head->next;
        new_head = new_head->next;
    }
    return head == NULL && new_head == NULL;
}