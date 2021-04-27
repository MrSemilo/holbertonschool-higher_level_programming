#include "lists.h"
/**
 *check_cycle - prototype
 *@list: cycle.
 *Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *var1;

	var1 = list;
	if (!list)
		return (0);

	while (list && var2 && var1->next)
	{
		var1 = var1->next->next;
		list = list->next;
		if (list == var1)
			return (1);
	}
	return (0);
}
