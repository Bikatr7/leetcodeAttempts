// Kaden Bilyeu (Bikatr7)
// 2024-09-08
// 725. Split Linked List in Parts (Medium)

// Description:
// Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
// The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
// The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
// Return an array of the k parts.

// Example 1:
// Input: head = [1,2,3], k = 5
// Output: [[1],[2],[3],[],[]]
// Explanation: The first element output[0] has output[0].val = 1, output[0].next = null.
// The last element output[4] is null, but its string representation as a ListNode is [].

// Example 2:
// Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
// Output: [[1,2,3,4],[5,6,7],[8,9,10]]
// Explanation: The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

// Constraints:
// The number of nodes in the list is in the range [0, 1000].
// 0 <= Node.val <= 1000
// 1 <= k <= 50

// Topics: Linked List

// Hints:
// Hint 1: If there are N nodes in the list, and k parts, then every part has N/k elements, except the first N%k parts have an extra one.

#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize)
{
    struct ListNode** result = (struct ListNode**)malloc(k * sizeof(struct ListNode*));
    *returnSize = k;

    int length = 0;
    struct ListNode* current = head;
    
    while (current != NULL)
    {
        length++;
        current = current->next;
    }
    
    int base_size = length / k;
    int extra = length % k;
    
    current = head;
    
    for (int i = 0; i < k; i++)
    {
        result[i] = current;
        
        int part_size = base_size + (i < extra);
        
        for (int ii = 1; ii < part_size && current != NULL; ii++)
        {
            current = current->next;
        }
        
        if (current != NULL)
        {
            struct ListNode* next = current->next;
            current->next = NULL;
            current = next;
        }
    }
    
    return result;
}