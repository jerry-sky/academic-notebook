from typing import Iterable


def XSYang(x: Iterable[float], epsilon_vector: Iterable[float]):
    """Calculate the X.S. Yang function value at `x` with `epsilon_vector`
    as the \\varepsilon parameter.
    """

    output = 0
    for i in range(0, 5):
        output += epsilon_vector[i] * ((abs(x[i]))**(i+1))

    return output
