#include <stdio.h>
#include "lists.h"
int palindrome(int *t, int len);
/**
 * palindrome - checks if a linked list is palindrome or not.
 * @head: first node.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
  listint_t *current = *head;
  int i = 0, t[2900];
  if (*head == NULL || (*head)->next == NULL)
    return (1);
  while (current)
    {
      t[i] = current->n;
      i++;
      current = current->next;
    }
  return (palindrome(t, i - 1));
}

/**
 * palindrome - checks whether a string is palindrome or not.
 * @t: array containing the numbers of the linked list.
 * @len: length of the array minus 1.
 * Return: 1 if it is palindrome, 0 if not
 */
int palindrome(int *t, int len)
{
 int i = 0;

 while (i < (len + 1) / 2)
    {
      if (t[i] != t[len - i])
        {
          return (0);
        }
      i++;
    }
  return (1);
}
