#include "lists.h"

/**
* insert_dnodeint_at_index - inserts a new node at a given position.
* @h : head
* @idx : index of the list where the new node should be added
* @n : number
* Return: the address of the new node, or NULL if it failed
*/

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new;
	dlistint_t *temp;
	unsigned int i;

	new = *h;
	if (h == NULL)
		return (NULL);

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	temp = *h;
	if (*h == NULL && idx == 0)
	{
		new->next = NULL;
		new->prev = NULL;
		*h = new;
	}
	for (i = 0 ; i < idx ; i++)
	{
		if (temp->next == NULL)
			return (NULL);
		temp = temp->next;
	}
	new->n = n;
	new->next = temp;
	if (idx > 0)
	{
		new->prev = temp->prev;
		temp = temp->prev;
		temp->next = new;
	}
	else
	{
		new->prev = NULL;
		temp->prev = new;
		*h = new;
	}
	return (new);
}
