#!/usr/bin/python3
"""Prime game"""


def is_prime(num):
    """Checks for prime number"""
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Checks who the winner is"""
    if x > len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for rounds in range(x):
        turn = 1
        choices = [n + 1 for n in range(nums[rounds])]
        i = 1

        while i < len(choices):
            num = choices[i]
            if is_prime(num):
                a = num
                choices.pop(i)
                k = 0
                while k < len(choices):
                    if choices[k] % a == 0:
                        choices.pop(k)
                    k += 1
                turn += 1
                i = 0
            i += 1
        if turn == 1:
            ben_wins += 1
        elif turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
