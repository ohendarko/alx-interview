#!/usr/bin/python3
"""Determine who the winner of each game is"""


def isWinner(x, nums):
    def sieve(n):
        """Generate primes up to n"""
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def simulate_game(n):
        """Simulate the game"""
        primes = sieve(n)
        if not primes:
            return "Ben"

        moves = 0
        current_set = set(range(1, n + 1))

        for prime in primes:
            if prime in current_set:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    if multiple in current_set:
                        current_set.remove(multiple)

        return "Maria" if moves % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
