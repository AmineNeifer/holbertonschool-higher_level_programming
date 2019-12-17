#include <stdio.h>
#include "lists.h"
int palindrome(int *t, int len);
/**
 *
 *
 *
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
  listint_t *current = *head;
  int i = 0, t[50];
  if (*head == NULL || (*head)->next == NULL)
    return (1);
  while (current && current->next)
    {
      t[i] = current->n;
      i++;
      current = current->next;
    }
  return (palindrome(t, i -1));
}

/**
 * palindrome - checks whether a string is palindrome or not.
 *
 *
 * Return: 1 if it is palindrome, 0 if not
 */
int palindrome(int *t, int len)
{
 int i = 0;

  while (i < (len + 1) / 2)
    {
      if (t[i] != t[len - i])
        {
          return (1);
        }
      i++;
    }
  return (0);
}
