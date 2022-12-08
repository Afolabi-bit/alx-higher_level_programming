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
	if (*head == NULL) /* Case: Empty list */
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n) /* Case: Insert at the beginning */
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	/* Insert in between or at the end, even multiple nodes */
	{
		temp = *head;
		while (temp->next != NULL && number > temp->next->n)
		{
			temp = temp->next;
		}
		new->n = number;
		new->next = temp->next;
		temp->next = new;
		return (new);
	}
	free(temp);
	return (NULL);
}
