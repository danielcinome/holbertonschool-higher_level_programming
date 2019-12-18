#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head : head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *sta;
	int len = 0, i = 0;
	int str[9999];

	if (*head == NULL)
		return (1);
	sta = *head;
	while (sta)
	{
		str[i] = sta->n;
		sta = sta->next;
		i++;
	}
	len = i;
	for (i = 0 ; i != len ; i++)
	{
		len--;
		if (str[i] != str[len])
			return (0);
		if (i == len)
			break;
	}
	return (1);
}
