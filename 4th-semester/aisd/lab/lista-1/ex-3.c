#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

/**
 * A node of a two-way cyclical list.
 */
typedef struct __list_node__
{
  /**
   * The actual value that is being held by the list node.
   */
  int value;
  /**
   * Points to the next node in the list.
   */
  struct __list_node__ *next;
  /**
   * Points to the previous node in the list.
   */
  struct __list_node__ *prev;
} ListNode;

/**
 * Add a new value to the list.
 */
void push(int value, ListNode **node)
{
  ListNode *new_node = malloc(sizeof(ListNode));
  new_node->value = value;

  if ((*node) == NULL)
  {
    new_node->next = new_node;
    new_node->prev = new_node;
    (*node) = new_node;
    return;
  }

  ListNode *prev = (*node);
  ListNode *next = prev->next;

  new_node->next = next;
  new_node->prev = prev;

  prev->next = new_node;
  next->prev = new_node;
}

/**
 * Merge two lists into one.
 */
ListNode *merge(ListNode *one, ListNode *two)
{

  if (one == NULL)
  {
    return two;
  }

  if (two == NULL)
  {
    return one;
  }

  one->next = two;
  two->prev = one;

  ListNode *lastOfTwo = two->next;
  while (lastOfTwo->next != two)
  {
    lastOfTwo = lastOfTwo->next;
  }
  ListNode *lastOfOne = one->prev;
  while (lastOfOne->prev != one)
  {
    lastOfOne = lastOfOne->prev;
  }

  lastOfOne->prev = lastOfTwo;
  lastOfTwo->next = lastOfOne;
}

/**
 * Check if the provided value is in the provided list.
 */
bool isIn(int value, ListNode *node)
{
  if (node == NULL)
  {
    return false;
  }

  ListNode *root = node;
  ListNode *current = node;

  do
  {
    if (current->value == value)
    {
      return true;
    }
    current = current->next;
  } while (current->next != root);
  return false;
}

/**
 * Example program implementing the two-way cyclical list.
 */
int main(int argc, char const *argv[])
{
  // prepare the clock
  clock_t begin;
  clock_t end;
  // prepare the random number generator
  time_t t;
  srand((unsigned)time(&t));

  ListNode *list = NULL;

  for (int i = 0; i < 1000; i++)
  {
    push(rand() % 1000, &list);
  }

  // measure predefined numbers
  begin = clock();
  isIn(512, list);
  end = clock();
  double time_spent_predefined = (double)(end - begin) / CLOCKS_PER_SEC;

  // measure random numbers
  begin = clock();
  isIn(rand() % 1000, list);
  end = clock();
  double time_spent_random = (double)(end - begin) / CLOCKS_PER_SEC;

  printf("\nexecution time with predefined : %es\n", time_spent_predefined);
  printf("execution time with random     : %es\n", time_spent_random);

  // test merging two lists
  ListNode *one = NULL;
  push(3, &one);
  push(7, &one);
  ListNode *two = NULL;
  push(4, &two);
  push(8, &two);

  ListNode *merged = merge(one, two);

  printf("merged list:\n");
  ListNode *current = merged;
  do
  {
    printf("%d\n", current->value);
    current = current->next;
  } while (current != merged);

  return 0;
}
