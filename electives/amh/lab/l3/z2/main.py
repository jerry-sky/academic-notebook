#!/usr/bin/env python3
from random import randint, random
from time import time
from sys import stderr, exit
from typing import Dict, Iterable, Set
from copy import copy


def calc_word_score(word, letters_count, letters_score):
    """Evaluate word's score. If the word contains letters outside provided scope,
    the output will be \infty.
    """

    output = 0
    # keep track of the used letters
    letters_remaining = dict(letters_count)

    for w in word:
        if w not in letters_count:
            # contains a letter outside the provided scope
            return 0
        if letters_remaining[w] == 0:
            # too many occurrences of that letter
            return 0
        output += letters_score[w]
        letters_remaining[w] -= 1

    return output


def get_random_letter(available_letters: Iterable[str]) -> str:
    return available_letters[randint(0, len(available_letters)-1)]


def generate_population(founding_fathers: Iterable[str], max_pop_size: int,
                        mutation_probability: float, additional_letters_probability: float,
                        available_letters: Iterable[str]):

    population = set(founding_fathers)
    # generate remaining population members based on the „founding fathers”
    while len(population) < max_pop_size:
        # pick two parents to crossover
        p_one = founding_fathers.pop(randint(0, len(founding_fathers)-1))
        p_two = founding_fathers[randint(0, len(founding_fathers)-1)]
        founding_fathers.append(p_one)
        # take a part from the first parent
        index = randint(1, len(p_one)-1)
        part_one = p_one[:index]
        if random() > 0.5:
            part_one = p_one[index:]
        # take a part from the second parent
        index = randint(1, len(p_two)-1)
        part_two = p_two[index:]
        if random() > 0.5:
            part_two = p_two[:index]

        new_member = part_one + part_two

        # mutation stage
        # provide a possibility to add a new letter at the front or
        # at the end of the word
        new_member = ' ' + new_member + ' '
        # `str`s are immutable so we need to have a list to alter the new member
        new_member_list = list(new_member)
        # iterate over all new member's letters
        for i in range(0, len(new_member_list)):
            if new_member_list[i] == ' ':
                if random() > 1-additional_letters_probability:
                    new_member_list[i] = get_random_letter(available_letters)
            else:
                if random() > 1-mutation_probability:
                    l = new_member_list[i]
                    while l == new_member_list[i]:
                        l = get_random_letter(available_letters)
                    new_member_list[i] = l

        new_member = ''.join(new_member_list)

        population.add(new_member.strip())

    return population


def GA_dict_score_search(dict_: Set[str], letters_score: Dict[str, int],
                         letters_count: Dict[str, int], initial_solutions: Iterable[str],
                         max_pop_size: int, mutation_probability: float,
                         additional_letters_probability: float, max_running_time: int):

    begin = time()

    available_letters = list(letters_count.keys())

    # generate the first population
    population = [*initial_solutions]

    end = time()
    while end-begin <= max_running_time:

        # selection stage
        pivot = round(max_pop_size/3)
        founding_fathers = population[:pivot]
        # additionally, select a few from the rest just to shake things up
        # (to increase gene diversity)
        the_rest = population[pivot:]
        if len(population) == max_pop_size:
            for _ in range(3):
                founding_fathers.append(the_rest.pop(randint(0, len(the_rest)-1)))

        # generate a new population
        population = generate_population(
            founding_fathers, max_pop_size,
            mutation_probability, additional_letters_probability,
            available_letters)

        population = sorted(population, key=lambda word: calc_word_score(
            word, letters_count, letters_score) if word in dict_ else 0, reverse=True)

        end = time()

    return population[0]


if __name__ == '__main__':

    dict_ = set()

    # read the dictionary entries
    with open('dict.txt', 'r') as f:
        t = f.readline()
        while t:
            t = t[:-1].lower()
            dict_.add(t)
            t = f.readline()

    # read data from stdin
    t, n, s = map(lambda x: int(x), input().split())

    letters_score = dict()
    letters_count = dict()
    for _ in range(0, n):
        c, p = input().split()
        letters_score[c] = int(p)
        if c in letters_count:
            letters_count[c] += 1
        else:
            letters_count[c] = 1

    initial_solutions = list()
    for _ in range(0, s):
        s = input().strip()
        initial_solutions.append(s)

    result = GA_dict_score_search(dict_=dict_, letters_score=letters_score,
                                  letters_count=letters_count, initial_solutions=initial_solutions,
                                  max_pop_size=600, mutation_probability=0.05,
                                  additional_letters_probability=0.1, max_running_time=t)
    print(result, file=stderr, end='')
    print(calc_word_score(result, letters_count, letters_score))
