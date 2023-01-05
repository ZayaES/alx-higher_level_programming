#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	else
	{
		if (number < current->n)
		{
			new->next = *head;
			*head = new;
			return (*head);
		}
		while ((number > current->next->n))
		{
			current = current->next;
			if (current->next == NULL)
				break;
		}
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
