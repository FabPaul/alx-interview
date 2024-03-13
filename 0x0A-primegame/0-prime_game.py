#!/usr/bin/python3
"""Prime game"""


def is_prime(num):
    """Checks for prime numbers"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Checks who the winner is"""
    if not nums or x < 1:
        return None

    max_value = max(nums)
    prime_flags = [is_prime(i) for i in range(max(max_value + 1, 2))]

    cumulative_primes = 0
    for i in range(len(prime_flags)):
        if prime_flags[i]:
            cumulative_primes += 1
        prime_flags[i] = cumulative_primes

    player_score = 0
    for num in nums:
        player_score += prime_flags[num] % 2 == 1

    if player_score * 2 == len(nums):
        return None
    if player_score * 2 > len(nums):
        return "Maria"
    return "Ben"
