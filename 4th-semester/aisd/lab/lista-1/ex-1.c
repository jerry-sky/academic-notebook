#include <stdio.h>
#include <stdlib.h>

struct fifo_node
{
  int value;
  struct fifo_node *next;
  struct fifo_node *prev;
};

int pop(struct fifo_node *node)
{
  struct fifo_node *current = node;
  while (current->next != NULL)
  {
    current = current->next;
  }
  int value = current->value;
  current->prev->next = NULL;

  return value;
}

void push(struct fifo_node *node, int value)
{
  printf("init push %d\n", value);
  struct fifo_node *current = node;
  printf("before while push %d\n", value);
  while (current->prev != NULL)
  {
    printf("in: while %d\n", value);
    current = current->prev;
  }
  printf("after while %d\n", value);
  struct fifo_node new_node = {
      .value = value,
      .prev = NULL,
      .next = current};

  printf("before saving %d\n", value);

  current->prev = &new_node;
  
  printf("saved %d\n", value);
}

int main(int argc, char const *argv[])
{

  struct fifo_node fifo = {.value = 1, .next = NULL, .prev = NULL};

  push(&fifo, 2);
  push(&fifo, 3);
  push(&fifo, 4);
  push(&fifo, 5);

  // printf("%d, %d\n", fifo.value, fifo.prev->value);
  // printf("%d", pop(&fifo));

  return 0;
}
