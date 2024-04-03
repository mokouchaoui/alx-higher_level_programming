#include "lists.h"

/**
 * insert_node - Inserts a num into a sorted singly linked list in.
 * @head: Apoint to the head of the listint_t list.
 * @num: The num to be inserted.
 * Author - Mohamed Kouchaoui
 * Return: If the func fails should return NULL.
 *         Otherwise - the address of the new node.
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = num;

	if (node == NULL || node->n >= num)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < num)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
