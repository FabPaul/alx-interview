#!/usr/bin/python3
""" Minim operations """


def minOperations(n):
    """
    Function that calculates the fewest ops needed to result in
    exactly n H characters in a file
    """

    # If n is impossible to achieve, return 0
    if n <= 2:
        return 0

    operations = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
            divisor -= 1

        divisor += 1

    return operations
