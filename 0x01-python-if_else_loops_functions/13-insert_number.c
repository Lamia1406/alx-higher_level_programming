#include "lists.h"
#include <stdlib.h>

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
	while (temp_head && temp_head->next->n < number)
		temp_head = temp_head->next;
	node->next = temp_head->next;
	temp_head->next = node;
	return (node);
}
