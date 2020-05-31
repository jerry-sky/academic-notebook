#!/usr/bin/env python3
import numpy as np
from sys import exit, argv
np.random.seed(17)


def relu(x):
    return x * (x > 0)


def relu_derivative(x):
    return 1. * (x > 0)


def sigmoid(x):
    return 1. / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1. - x)


class NeuralNetwork(object):

    def __init__(self, x, y, eta, func1, func2, func1_derivative, func2_derivative):
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta

        self._func1 = func1
        self._func2 = func2
        self._func1_derivative = func1_derivative
        self._func2_derivative = func2_derivative

    def feedforward(self):
        self.layer1 = self._func1(np.dot(self.input, self.weights1.T))
        self.output = self._func2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self._func2_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        delta1 = self._func1_derivative(self.layer1) * \
            np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == "__main__":

    if len(argv) < 2:
        exit('usage: ./ex-1.py <XOR|OR|AND>')

    operation = argv[1]

    runs = [
        # (eta, func1, func2, func1 derivative, func2 derivative), comment
        ((0.0001, relu, relu, relu_derivative, relu_derivative),
         r'all relu, eta=0.0001; when rounded to nearest integer it gives good results; '
         r'curiously – the results are sometimes about 0.25 too high'),
        ((0.01, sigmoid, relu, sigmoid_derivative, relu_derivative),
         r'sigmoid & relu, eta=0.01; not that great, but still rounding it gives good results'),
        ((0.01, relu, sigmoid, relu_derivative, sigmoid_derivative),
         r'relu & sigmoid, eta=0.01; very close to the actual sought value'),
        ((0.1, sigmoid, sigmoid, sigmoid_derivative, sigmoid_derivative),
         r'all sigmoid, eta=0.1; interestingly, for very high eta (>20) „OR” and „XOR” '
         r'operation had almost 100% accurate results; but it was unstable for „AND”; '),
    ]

    for run in runs:
        X = np.array([
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ])
        # a column of ones is neccessary to include a bias

        # define the „correct” answer
        y = np.array([[0], [1], [1], [0]])

        # other operations
        if operation == 'OR':
            y = np.array([[0], [1], [1], [1]])
        elif operation == 'AND':
            y = np.array([[0], [0], [0], [1]])

        nn = NeuralNetwork(X, y, *run[0])

        # train the neural network
        for _ in range(5000):
            nn.feedforward()
            nn.backprop()

        np.set_printoptions(precision=3)
        # print the output
        print(nn.output)
        # print the comment
        print(run[1])
        print()
