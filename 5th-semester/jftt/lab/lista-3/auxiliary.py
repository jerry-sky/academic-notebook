
Zp = 1234577

def flatten(x: int) -> int:
    '''
    Flattens a number to be an element from the \mathbb{Z}_p field.
    '''
    return ((x % Zp) + Zp) % Zp


def multiply(x: int, y: int) -> int:
    '''
    Multiplies two numbers in the field \mathbb{Z}_p.
    '''
    output = flatten(x)
    for i in range(1, y):
        output += x
        output = flatten(output)
    return output


def inverse(a: int) -> int:
    '''
    Finds the opposite number to the one given inside the \mathbb{Z}_p field.
    '''
    m = Zp
    x = 1
    y = 0

    while a > 1:
        quotient = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - quotient * y
        x = t

    if x < 0:
        x += Zp

    return x

def print_(*x) -> None:
    '''
    Prints given arguments without the newline at the end.
    '''
    print(*x, end='')
