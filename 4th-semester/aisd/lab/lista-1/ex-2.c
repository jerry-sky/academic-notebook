#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

/**
 * A node of a one-way list.
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
} ListNode;

/**
 * Check if the provided value is in the provided list.
 */
bool isIn(int value, ListNode *node)
{
  if (node == NULL)
  {
    return false;
  }
  ListNode *current = node;
  do
  {
    if (current->value == value)
    {
      return true;
    }
    current = current->next;
  } while (current->next != NULL);

  return false;
}

/**
 * Add a new value to the list.
 */
void push(int value, ListNode **node)
{
  if ((*node) == NULL)
  {
    (*node) = malloc(sizeof(ListNode));
    (*node)->value = value;
  }
  ListNode *current = (*node);
  while (current->next != NULL)
  {
    current = current->next;
  }

  current->next = malloc(sizeof(ListNode));
  current->next->value = value;
}

/**
 * Merge two lists together into one.
 */
ListNode *merge(ListNode *one, ListNode *two)
{

  ListNode *merged = one;
  if (merged == NULL)
  {
    return two;
  }

  ListNode *lastOfOne = one;
  while (lastOfOne->next != NULL)
  {
    lastOfOne = lastOfOne->next;
  }
  lastOfOne->next = two;
}

/**
 * A program that implements the one-way list.
 */
int main(int argc, char const *argv[])
{
  // prepare the clock
  clock_t begin;
  clock_t end;
  // prepare the random number generator
  time_t t;
  srand((unsigned)time(&t));

  // preload the list with random arbitrary numbers
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
  ListNode *one = malloc(sizeof(ListNode));
  one->value = 1;
  ListNode *two = malloc(sizeof(ListNode));
  two->value = 2;

  ListNode *merged = merge(one, two);

  printf("merged list:\n");
  ListNode *current = merged;
  while (current != NULL)
  {
    printf("%d\n", current->value);
    current = current->next;
  }

  return 0;
}
