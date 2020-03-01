#include <stdio.h>
#include <stdlib.h>

/**
 * A container that holds an arbitrary value and pointers to nodes adjacent to this node.
 */
typedef struct __fifo_node__
{
  int value;
  // struct __fifo_node__ *next;
  struct __fifo_node__ *prev;
} fifoNode;

/**
 * Return value of the first inserted node and remove it from the FIFO chain.
 */
int pop(fifoNode **node)
{
  // get the value
  int value = (*node)->value;

  // reconnect the pointer to point to a new last node
  fifoNode *new_head = (*node)->prev;
  // remove said node
  free((*node));
  (*node) = new_head;

  return value;
}

/**
 * Add a new node with the provided arbitrary value.
 */
void push(fifoNode **node, int value)
{
  // handle null node
  if ((*node) == NULL)
  {
    // begin a new FIFO chain
    (*node) = malloc(sizeof(fifoNode));
    (*node)->value = value;
    return;
  }
  // loop through and find the last inserted node
  fifoNode *current = (*node);

  // return;
  while (current->prev != NULL)
  {
    current = current->prev;
  }

  // create a new node with provided arbitrary value
  fifoNode *new_node = NULL;
  new_node = (fifoNode *)malloc(sizeof(fifoNode));
  new_node->value = value;
  new_node->prev = NULL;
  // new_node->next = current;

  // insert said new node into the chain
  current->prev = new_node;
}

/**
 * A program that exemplifies a use-case for the FIFO chain.
 */
int main(int argc, char const *argv[])
{

  fifoNode *fifo = NULL;
  // fifo = (fifoNode *)malloc(sizeof(fifoNode));
  // fifo->value = 1;
  push(&fifo, 2);
  printf("%d\n", fifo->value);
  // return 0;
  push(&fifo, 3);
  push(&fifo, 4);
  push(&fifo, 5);

  printf("%d, %d\n", fifo->value, fifo->prev->value);
  printf("pop: %d\n", pop(&fifo));
  printf("pop: %d\n", pop(&fifo));
  // printf("pop: %d\n", pop(&fifo));
  // printf("pop: %d\n", pop(&fifo));

  fifoNode *current = NULL;
  current = fifo;
  while (current->prev != NULL)
  {
    printf("value: %d\n", current->value);
    current = current->prev;
  }

  return 0;
}
