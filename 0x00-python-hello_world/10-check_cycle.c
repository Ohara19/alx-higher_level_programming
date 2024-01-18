#include "lists.h"

/**
 * check a cycle  a function that check if a list has a cycle
 * the linked list
 * return 1 if there is a cycle and 0 if not
 */
int check_cycle(listint_t *list);
{
	listint_t *fast *slow;

	if (!list || !list->next)
		return (0);
	fast = list->next->next;
	slow = list;
	
	while (slow != NULL && fast != NULL && fast-> != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{	
		return (1);
		}
	}
	return (0);
}
