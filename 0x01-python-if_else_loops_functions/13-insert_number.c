#include "lists.h"

/**
 * insert_node - Inserts a number into
 * a sorted singly linked list
 * @head: pointer to list head
 * @number: number to be inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		temp = *head;
		while (temp)
		{
			if (temp->next->n > new->n)
			{
				new->next = temp->next;
				temp->next = new;
				return (new);
			}
			temp = temp->next;
		}
	}
	free(temp);
	return (NULL);
}
