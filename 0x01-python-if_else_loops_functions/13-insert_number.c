#include "lists.h"

/**
* insert_node - check the code for Holberton School students.
* @head : head
* @number : number
* Return: Always 0.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	if (head == NULL)
		return (NULL);

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		new->n = number;
	}

	while (temp != NULL)
	{
		if (temp->n > number)
		{
			new->next = *head;
			*head = new;
			new->n = number;
			break;
		}
		else if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			new->n = number;
			break;
		}
		temp = temp->next;
	}
	return (new);
}
