"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?"""


def is_prime(num):
    n = int(num ** 0.5) + 1
    while n > 1:
        if num % n == 0:
            return False
        n -= 1
    return True


n = 3
primes = [2]

while len(primes) < 10001:
    if is_prime(n):
        primes.append(n)
        print "prime # {:,}: {:}".format(len(primes), n)
    n += 2
