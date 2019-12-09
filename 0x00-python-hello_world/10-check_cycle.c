#include "lists.h"

/**
 * check_cycle - check the code for Holberton School students.
 * @list : header
 * Return: 0 Linked list has no cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}
	return (0);
}
