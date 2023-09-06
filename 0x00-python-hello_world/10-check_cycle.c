include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: int
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, **nodes;
	int c = 0, i = 0, j;

	while (head)
	{
		c++;
		head = head->next;
	}
	nodes = malloc(sizeof(listint_t *) * c);
	if (nodes == NULL)
		return (0);
	head = list;
	while (head)
	{
		for (j = 0; j < i; j++)
		{
			if (head == nodes[j])
			{
				free(nodes);
				return (1);
			}
		}
		nodes[i] = head;
		head = head->next;
		i++;
	}
	free(nodes);
	return (0);
}

