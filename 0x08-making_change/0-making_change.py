#!/user/bin/python3

"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """returns fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    coins.sort()
    balance = 0
    for coin in coins[:: -1]:
        if total <= 0:
            break
        temp = total // coin
        balance += temp
        total -= (temp * coin)

    if total != 0:
        return -1

    return balance