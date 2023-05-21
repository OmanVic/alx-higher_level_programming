#include "lists.h"
/**
 * check_cycle - check if a single linked list has a cycle
 *
 * @list: pointer to the head of the linkedlist to be checked
 *
 * Return: 0 if there is no cycle, otherwise 1
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;
	if (!ptr)
		return (0);
	while (ptr)
	{
		ptr = ptr->next;
		if (ptr == NULL)
			return (0);
		else if (ptr == list)
			break;
	}
	return (1);
}
