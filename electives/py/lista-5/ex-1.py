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

    return predicted_reviews


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

    return predicted_reviews


if __name__ == '__main__':

    data = pd.read_csv('data/ratings.csv')

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
    matrix_X = filtered[['newUserId', 'movieId', 'rating']
                        ].sort_values(by='rating')

    # make it an actual matrix
    matrix_X = pd.pivot_table(
        matrix_X, values='rating', index='newUserId', columns=['movieId']).to_numpy()

    # fill out the rest of the matrix with zeroes
    matrix_X = np.nan_to_num(matrix_X, nan=0)

    # sort the matrix by the first column for easier data evaluation
    # and more clear data visualisation
    sorted_indicies = np.argsort(matrix_X[:, 0])
    matrix_X = matrix_X[sorted_indicies]

    # take the first column (that's the movie rating that we're analysing)
    matrix_Y = matrix_X[:, [0]]

    data_set_sizes = [10, 1000, 10000]
    predicted_reviews_across_data_set_sizes = []

    for data_set_size in data_set_sizes:
        # take the part we're analysing
        matrix_X_local = matrix_X[:, 1:data_set_size+1]

        predicted_reviews_across_data_set_sizes.append(
            estimate_using_linalg(matrix_X_local, matrix_Y)
        )

    # plot the results
    x = list(range(215))

    fig, ax = plt.subplots(2)

    ax[0].plot(x, predicted_reviews_across_data_set_sizes[0], label='m='+str(
        data_set_sizes[0]), linewidth=0.4, linestyle='dashed')

    for i in range(1, len(data_set_sizes)):
        ax[0].plot(
            x, predicted_reviews_across_data_set_sizes[i], label='m='+str(data_set_sizes[i]), linewidth=2)

    ax[0].plot(x, matrix_Y[:, 0], label='original reviews', linestyle='dotted', markersize=0.2)

    ax[0].legend()
    ax[0].set_title('Podpunkt 1)')

    # now, we want to take first 200 people and estimate ratings for
    # the rest of 15 people based on that data
    matrix_X_200 = matrix_X[:200, :]
    matrix_Y_200 = matrix_X_200[:, [0]]

    to_test_X = matrix_X[200:, :]
    to_test_Y = to_test_X[:, [0]]

    data_set_sizes = [10, 100, 500, 1000, 10000]

    predicted_reviews_across_data_set_sizes_test = []

    for data_set_size in data_set_sizes:
        matrix_X_local = matrix_X_200[:, 1:data_set_size+1]
        to_test_X_local = to_test_X[:, 1:data_set_size+1]

        predicted_reviews_across_data_set_sizes_test.append(
            estimate_using_linalg_test(
                matrix_X_local, matrix_Y_200, to_test_X_local)
        )

    x = list(range(200, 215))

    ax[1].plot(x, predicted_reviews_across_data_set_sizes_test[0], label='m='+str(
        data_set_sizes[0]), linewidth=0.4, linestyle='dashed')

    for i in range(1, len(data_set_sizes)):
        ax[1].plot(
            x, predicted_reviews_across_data_set_sizes_test[i], label='m='+str(data_set_sizes[i]), linewidth=2)

    ax[1].plot(x, to_test_Y[:, 0], label='original reviews',
             markersize=0.2, linestyle='dotted')

    ax[1].legend()
    ax[1].set_title('Podpunkt 2)')

    plt.tight_layout()
    plt.show()
