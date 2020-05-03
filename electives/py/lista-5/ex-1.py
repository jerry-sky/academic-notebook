#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sys import exit

pd.options.mode.chained_assignment = None  # default='warn'


def get_regression_factors(matrix_X, matrix_Y):
    """Calculate the regression factors.
    """
    return np.linalg.lstsq(
        matrix_X, matrix_Y, rcond=None)[0][:, 0]
    # that part at the end of the above line flattens an array of
    # singleton arrays to a simple array of numbers


def estimate_using_linalg(matrix_X, matrix_Y):
    """Estimate users' ratings for a selected film based on their ratings
    of other movies.
    """
    predicted_reviews = []
    # do linear regression
    regression_factors = get_regression_factors(matrix_X, matrix_Y)

    # estimate the review
    for reviews in matrix_X:
        predicted_reviews.append(
            sum(reviews * regression_factors)
        )

    return np.array(predicted_reviews)


def estimate_using_linalg_test(matrix_X, matrix_Y, to_test):
    """Estimate ratings for a selected film based on ratings of other people.
    """
    predicted_reviews = []
    regression_factors = get_regression_factors(matrix_X, matrix_Y)

    # estimate other people's reviews
    for reviews in to_test:
        predicted_reviews.append(
            sum(reviews * regression_factors)
        )

    return np.array(predicted_reviews)


if __name__ == '__main__':

    # get the data
    data = pd.read_csv('data/ratings.csv')

    # parse the timestamps
    data.timestamp = data.timestamp.map(lambda x: datetime.fromtimestamp(x))

    # get ids of the people that have reviewed Toy Story
    filtered = data.loc[data['movieId'] == 1]
    people_ids = set()
    for x in filtered.to_dict('records'):
        people_ids.add(x.get('userId'))
    people_ids = list(people_ids)

    # get records for movies that were reviewed by people that also reviewed
    # Toy Story
    filtered = data.loc[data['userId'].isin(people_ids)]

    # create a new column for the `i` index in the new „people that reviewed
    # Toy Story” data slice
    filtered['newUserId'] = filtered['userId'].map(
        lambda x: people_ids.index(x))

    # take the part we need
    filtered = filtered[['newUserId', 'movieId', 'rating']]

    # prepare matrix that can take up to 10000 movies
    # offsetting by 2, because `movieId=0` doesn't exist
    # and `movieId=1` is the one movie we're analysing
    matrix_X = np.zeros((filtered['newUserId'].max() + 1, 10000 + 2))
    # go through the records and write the actual data
    # to the prepared matrix
    for movie in filtered.to_dict('records'):
        # avoid `index out of bounds` exceptions
        if movie['movieId'] < len(matrix_X[0]):
            matrix_X[movie['newUserId'], movie['movieId']] = movie['rating']

    # take the first column containing the Toy Story reviews
    matrix_Y = matrix_X[:, [1]]
    # remove the first column containing the Toy Story reviews
    matrix_X = matrix_X[:, 2:]

    # measure by different data sizes
    data_set_sizes = [10, 1000, 10000]
    predicted_reviews_across_data_set_sizes = []

    for data_set_size in data_set_sizes:
        # take the part we're analysing
        matrix_X_local = matrix_X[:, :data_set_size]

        predicted_reviews_across_data_set_sizes.append(
            estimate_using_linalg(matrix_X_local, matrix_Y)
        )

    # plot the results
    x = list(range(0, 215))

    fig, ax = plt.subplots(2)

    # sort the matrix by the first column for easier data evaluation
    # and more clear data visualisation
    sorted_indicies = np.argsort(matrix_Y[:, 0])

    ax[0].plot(x, matrix_Y[:, 0][sorted_indicies], 'o',
               label='original reviews', markersize=5)

    # plot styles for each data set size
    plt_settings = [
        {'linewidth': 0.4, 'linestyle': 'dashed'},
        {'linewidth': 4},
        {'linewidth': 2}
    ]

    for i in range(0, len(data_set_sizes)):
        ax[0].plot(
            x, predicted_reviews_across_data_set_sizes[i][sorted_indicies], label='m='+str(data_set_sizes[i]), **plt_settings[i])

    ax[0].legend()
    ax[0].set_title('All predicted + original reviews')

    # now, we want to take first 200 people and estimate ratings for
    # the rest of 15 people based on that data
    matrix_X_200 = matrix_X[:200, :]
    matrix_Y_200 = matrix_X_200[:, [0]]

    # the last 15 people's data
    to_test_X = matrix_X[200:, :]
    to_test_Y = matrix_Y[200:, [0]]

    # test against different quantity of movies' ratings
    data_set_sizes = [10, 100, 200, 500, 1000, 10000]

    predicted_reviews_across_data_set_sizes_test = []

    for data_set_size in data_set_sizes:
        matrix_X_local = matrix_X_200[:, :data_set_size]
        to_test_X_local = to_test_X[:, :data_set_size]

        predicted_reviews_across_data_set_sizes_test.append(
            estimate_using_linalg_test(
                matrix_X_local, matrix_Y_200, to_test_X_local)
        )

    # plot the second part of this exercise

    x = list(range(200, 215))

    # sort the matrix by the first column for easier data evaluation
    # and more clear data visualisation
    sorted_indicies = np.argsort(to_test_Y[:, 0])

    ax[1].plot(x, to_test_Y[:, 0][sorted_indicies], 'o', label='original reviews',
               markersize=10)

    # plot styles for each data set size
    plt_settings = [
        {'linewidth': 8},
        {'linewidth': 5},
        {'linewidth': 2},
        {'linewidth': 2},
        {'linewidth': 2},
        {'linewidth': 2},
    ]

    for i in range(0, len(data_set_sizes)):
        ax[1].plot(
            x, predicted_reviews_across_data_set_sizes_test[i][sorted_indicies], label='m='+str(data_set_sizes[i]), **plt_settings[i])

    ax[1].legend()
    ax[1].set_title(
        'Predicted last 15 people\'s reviews based on first 200 people\'s reviews')

    plt.tight_layout()
    plt.show()
