#include "lists.h"

/**
* free_dlistint - free a list
* @head : head
*/

void free_dlistint(dlistint_t *head)
{
	dlistint_t *lib;
	dlistint_t *temp;

	lib = head;
	if (head->next != NULL)
	{
		while (temp)
		{
			temp = lib->next;
			free(lib);
			lib = temp;
		}
	}
	else
	{
		while (head)
		{
			temp = lib->prev;
			free(lib);
			lib = temp;
		}
	}
}
