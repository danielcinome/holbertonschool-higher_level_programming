#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *ite, *sta;
	int len = 0, i, j;

	if (head == NULL)
		return (0);
	sta = *head;
	while (sta)
	{
		sta = sta->next;
		len++;
	}
	sta = *head;
	ite = *head;
	for (i = 1 ; i != len ; i++)
	{
		for (j = 1 ; j < len ; j++)
		{
			ite = ite->next;
		}
		if (sta->n != ite->n)
		{
			return (0);
		}
		else
		{
			sta = sta->next;
			if (sta == ite)
				break;
			ite = *head;
			len--;
		}
	}
	return (1);
}
