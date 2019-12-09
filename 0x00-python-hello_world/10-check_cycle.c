#include "lists.h"

/**
 * check_cycle - check the code for Holberton School students.
 * @list : header
 * Return: 0 Linked list has no cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = list;
	temp2 = list;
	while (temp1)
	{
		while (temp2)
		{
			temp2 = temp2->next;
			if (temp1 == temp2)
				return (1);
		}
		temp1 = temp1->next;
	}
	return (0);
}
