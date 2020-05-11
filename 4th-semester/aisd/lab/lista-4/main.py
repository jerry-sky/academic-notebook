#!/usr/bin/env python3
from bst import BST
from rbt import RBT
from hash_tables import HashTable
from llist import LList

from sys import exit, argv, stdin, stderr
from time import time

import re


def parse_input_strings(data: str) -> str:
    return re.sub(r'[^a-zA-Z]', '', data)


if __name__ == "__main__":

    data_structures = ['bst', 'rbt', 'hmap']

    if len(argv) < 3:
        exit('usage: ./main.py --type <' + '|'.join(data_structures) + '>')

    chosen_data_structure = argv[2]

    if argv[1] == '--type' and argv[2] not in data_structures:
        exit('invalid options')

    # default data structure
    data_structure = RBT()

    if chosen_data_structure == 'bst':
        data_structure = BST()
    elif chosen_data_structure == 'hmap':
        data_structure = HashTable(size=11549)

    # measure many different thigns
    actions_performed_count = dict()
    actions_performed_total_time = dict()
    actions_available = ['insert', 'load', 'delete',
                         'find', 'min', 'max', 'successor', 'inorder']
    for a in actions_available:
        actions_performed_count[a] = 0
        actions_performed_total_time[a] = 0

    # measure total program running time
    total_running_time = 0
    # remember the maximum amount of items stored
    max_items_stored = 0

    # execute each line given
    for line in stdin:
        # measure running time
        begin = time()

        # parse the inputted line
        input_data = line.split(' ', 1)
        action = input_data[0].replace('\n', '')
        data = None
        if len(input_data) > 1:
            data = input_data[1].replace('\n', '')

        # perform requested action
        if action == 'insert' and data is not None:
            parsed = parse_input_strings(data)
            if len(parsed) > 0:
                data_structure.insert(parsed)

        elif action == 'load':
            if data is None:
                print('file path is required')
            try:
                with open(data, 'r') as f:
                    for line in f:
                        for word in line.split():
                            parsed = parse_input_strings(word)
                            if len(parsed) > 0:
                                data_structure.insert(parsed)
            except FileNotFoundError as e:
                print('file not found', e)

        elif action == 'delete' and data is not None:
            data_structure.delete(data)

        elif action == 'find' and data is not None:
            print('1' if data_structure.find(data) is not None else '0')

        # following options are for BST and RBT only
        elif chosen_data_structure != 'hmap':
            if action == 'min':
                t = data_structure.minimum()
                if t is not None:
                    print(t.value)
                else:
                    print()

            elif action == 'max':
                t = data_structure.maximum()
                if t is not None:
                    print(t.value)
                else:
                    print()

            elif action == 'successor' and data is not None:
                t = data_structure.successor(data)
                if t is not None:
                    print(t.value)
                else:
                    print()

            elif action == 'inorder':
                for el in data_structure.inorder():
                    print(el, end=' ')
                print()

        # if valid action but not meant for HashTable print empty line
        elif action in actions_available:
            print()
        # else: no response on invalid actions
        end = time()

        total_running_time += end - begin

        if action in actions_available:
            actions_performed_total_time[action] += end - begin
            actions_performed_count[action] += 1

        if max_items_stored < data_structure.nodes_count:
            max_items_stored = data_structure.nodes_count

    print('total running time  :', total_running_time, file=stderr)
    print(file=stderr)
    for a in actions_available:
        print('times ' + a + ' ran:', actions_performed_count[a], 'for a total of', actions_performed_total_time[a], 'seconds', file=stderr)
    print(file=stderr)
    print('max items stored    :', max_items_stored)
    print('final items quantity:', data_structure.nodes_count)
