#!/usr/bin/env python3
from rbt import RBT
from llist import LList
from time import time

from random import randint

from sys import argv, exit

if __name__ == "__main__":

    if len(argv) < 2:
        exit('usage ./ex-1-hash-table-chained-tests.py <items quantity>')

    # initialize both structures
    llist = LList()
    rbt = RBT()

    # add this quantity of items
    items_count = int(argv[1])

    # measure insertion times
    llist_insert_times = []
    rbt_insert_times = []

    for i in range(items_count):
        # t = i
        t = randint(0, items_count)
        # measure insertion time of a linked list
        begin = time()
        llist.insert(t)
        end = time()
        llist_insert_times.append(end-begin)
        # measure insertion time of a RB-Tree
        begin = time()
        rbt.insert(t)
        end = time()
        rbt_insert_times.append(end-begin)

    # calculate the average insertion time
    llist_insert_times_avg = sum(llist_insert_times)/len(llist_insert_times)
    rbt_insert_times_avg = sum(rbt_insert_times)/len(rbt_insert_times)

    # measure searching time
    t = randint(0, items_count)
    begin = time()
    x = llist.find(t)
    end = time()

    llist_find_time = end - begin

    begin = time()
    x = rbt.find(t)
    end = time()

    rbt_find_time = end - begin

    print('llist insert avg:', llist_insert_times_avg)
    print('rbt insert avg  :', rbt_insert_times_avg)
    print('avg insert rate :', rbt_insert_times_avg/llist_insert_times_avg)
    print('rbt faster      :', rbt_insert_times_avg < llist_insert_times_avg)
    print()
    print('llist find time :', llist_find_time)
    print('rbt find time   :', rbt_find_time)
    print('rbt faster      :', rbt_find_time < llist_find_time)
