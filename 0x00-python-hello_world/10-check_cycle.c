#include "lists.h"
/**
 *check_cycle - prototype
 *@list: cycle.
 *Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *var1, *var2;

	var1 = var2 = list;

	while (var1 && var2 && var2->next)
	{
		var1 = var1->next;
		var2 = var2->next->next;

		if (var1 == var2)
			return (1);
	}
	return (0);
}
