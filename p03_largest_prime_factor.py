"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143"""


def find_factors(num=600851475143):
    n = int(num ** 0.5) + 1
    factors = []
    while n > 0:
        if num % n == 0:
            factors.append(n)
            factors.append(num / n)
        n -= 1
    return sorted(factors)


def find_largest_prime_factor(num=600851475143):

    factors = find_factors(num)

    factors.reverse()

    for factor in factors:
        factor_factors = find_factors(factor)
        if len(factor_factors) == 2:
            return factor

find_largest_prime_factor()
