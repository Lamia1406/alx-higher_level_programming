#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a node into a sorted linked list
 * @head: Pointer to a pointer to the head of the list
 * @number: The value to insert into the list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *temp_head = *head;

	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if ((*head)->next->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (temp_head)
	{
		if (temp_head->next == NULL)
		{
			node->next = NULL;
			temp_head->next = node;
			return (node);
		}
		else if (temp_head->next->n < number)
			temp_head = temp_head->next;
		else
			break;
}
	node->next = temp_head->next;
	temp_head->next = node;
	return (node);
}
