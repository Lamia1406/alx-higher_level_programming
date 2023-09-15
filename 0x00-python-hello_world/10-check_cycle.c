#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: int
 */

int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_steps;

	one_step = list;
	two_steps = list;
	while (two_steps != NULL && two_steps->next != NULL)
	{
		one_step = one_step->next;
		two_steps = two_steps->next->next;
		if (one_step == two_steps)
			return (1);
	}
	return (0);
}

