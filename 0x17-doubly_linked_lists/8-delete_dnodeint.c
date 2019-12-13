#include "lists.h"

/**
* insert_dnodeint_at_index - inserts a new node at a given position.
* @h : head
* @idx : index of the list where the new node should be added
* @n : number
* Return: the address of the new node, or NULL if it failed
*/

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *ant;
	dlistint_t *temp;
	unsigned int i;

	ant = *head;
	if (head == NULL)
		return (-1);

	temp = *head;
	for (i = 0 ; i < index ; i++)
	{
		if (temp->next == NULL)
			return (-1);
		temp = temp->next;
	}
	if (index > 0)
	{
		ant = temp->prev;
		ant->next = temp->next;
		free(temp);
	}
	else
	{
		if (index == 0)
		{
			*head = temp->next;
			free(temp);
		}
		else
		{
			free(*head);
		}
	}
	return (1);
}
