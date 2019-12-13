#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0, a = 0;

	if(h == NULL)
		return(0);

	while(h != NULL)
	{
		a = h->n;
		printf("%lu\n", a);
		h = h->next;
		i++;
	}
	return(i);
}
