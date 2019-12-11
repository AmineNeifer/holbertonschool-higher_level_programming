#include "lists.h"
int check_cycle(listint_t *list)
{
  listint_t *slow; 
  listint_t *fast;
  slow = list;
  fast = list;

  if (list == NULL)
      return (0);
  while (slow && fast)
    {
      fast = fast->next->next;
      slow = slow->next;
      if (fast == slow)
	return(1);
    }
  return (0);
}
