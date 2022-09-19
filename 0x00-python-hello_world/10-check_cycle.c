nclude <stdio.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 is there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *rear;

	if (list == NULL)
		return (0);

	head = list;
	rear = list;

	while (rear != NULL && rear->next != NULL)
	{
		head = head->next;
		rear = rear->next->next;

		if (head == rear)
			return (1);

	}
	return (0);
}
