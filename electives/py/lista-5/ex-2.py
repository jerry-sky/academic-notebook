#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sys import exit


def recommend(other_peoples_ratings, targets_ratings):
    """Recommends a movie based on movie ratings of other people and
    the target person's movie ratings.

    Args:
        `other_peoples_ratings`: A matrix where rows are people's ids
            and the columns are movies' ids and the matrix values are
            movie ratings.
        `targets_ratings`: Target person's movie ratings in a column vector.
    """

    # calc the normalized matrix
    other_peoples_ratings_norm = np.linalg.norm(
        other_peoples_ratings, axis=0)
    # to avoid `nan`s and zero-divisions use numpy's way of dividing matrices
    X = np.divide(
        other_peoples_ratings, other_peoples_ratings_norm,
        # don't divide by zero
        where=other_peoples_ratings_norm != 0,
        # fill out with zeroes
        out=np.zeros_like(other_peoples_ratings)
    )

    z = np.dot(
        X,
        targets_ratings / np.linalg.norm(targets_ratings)
    )

    Z = z / np.linalg.norm(z)

    results = np.dot(X.T, Z)

    # generate movies' ids
    movies_ids = np.array(range(0, len(results)))
    # sort the results
    sorted_indicies = np.argsort(results[:, 0])
    # return sorted movies' ids
    return movies_ids[sorted_indicies][::-1]


if __name__ == '__main__':

    # read data
    data = pd.read_csv('data/ratings.csv')

    # take only part of the data
    filtered = data.loc[data['movieId'] < 10000]
    filtered = filtered[['userId', 'movieId', 'rating']]

    # prepare a matrix for the input data
    movies_count = filtered['movieId'].max() + 1
    people_count = filtered['userId'].max() + 1
    other_peoples_ratings = np.zeros((people_count, movies_count))

    # write the data to the prepared matrix
    for movie in filtered.to_dict('records'):
        other_peoples_ratings[
            movie['userId'], movie['movieId']
        ] = movie['rating']

    # an example of one's movie ratings
    my_ratings = np.zeros((movies_count, 1))

    my_ratings[2571] = 5      # 2571 - Matrix
    my_ratings[32] = 4        # 32 - Twelve Monkeys
    my_ratings[260] = 5       # 260 - Star Wars IV
    my_ratings[1097] = 4      # 1097 - E.T.

    # get the movies names
    movies_names_raw = pd.read_csv('data/movies.csv')
    movies_names_raw = movies_names_raw.loc[movies_names_raw['movieId'] < 10000]
    movies_names = ['' for _ in range(0, movies_count)]
    for movie in movies_names_raw.to_dict('records'):
        movies_names[movie['movieId']] = movie['title']

    # print the first 8 recommendations
    print('Recommended first 8 movies:')
    i = 1
    for movie in recommend(other_peoples_ratings, my_ratings)[:8]:
        print(str(i) + '.', movies_names[movie])
        i += 1
