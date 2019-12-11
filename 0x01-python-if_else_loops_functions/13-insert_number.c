#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new;
  listint_t *current;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);
  current =malloc(sizeof(listint_t));
  if (current == NULL)
    return (NULL);

  new->n = number;
  new->next = NULL;
  current = *head;

  while (current)
    {
      current = current->next;
      if (new->n <= current->next->n)
	{
	  new->next = current->next;
	  current->next = new;
	  return (new);
	}
    }
  return (NULL);
}
