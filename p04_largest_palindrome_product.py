"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def get_palindromes(high=999, low=100):
    n = high * high
    low = low * low

    palindromes = []

    while n >= low:
        if str(n) == str(n)[::-1]:
            palindromes.append(n)
        n -= 1

    return palindromes


def find_largest_palindrome(high=999, low=100):

    palindromes = get_palindromes(high, low)

    for palindrome in palindromes:
        n = int(palindrome ** 0.5) + 1
        while n >= low:
            if palindrome % n == 0 and (palindrome / n) >= low and (palindrome / n) <= high:
                print n
                print palindrome / n
                return palindrome
            n -= 1
