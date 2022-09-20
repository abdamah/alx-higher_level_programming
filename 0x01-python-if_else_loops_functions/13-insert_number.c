nclude <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *count;
	listint_t *new;

	count = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return(new);
	}

	while(count->next != NULL)
	{
		if ((count->next)->n >= number)
		{
			new->next = count->next;
			count->next = new;
			return(new);
		}
		count = count->next;
	}

	new->next = NULL;
	count->next = new;
	return(new);
}
