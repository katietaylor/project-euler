"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def find_largest_palindrome(high=999, low=100):

    largest_palindrome = 0
    n = high

    while n >= low:
        m = n
        if n * m < largest_palindrome:
            break

        while m >= low:
            product = n * m
            if product < largest_palindrome:
                break

            if str(product) == str(product)[::-1]:
                largest_palindrome = max([largest_palindrome, product])
                break

            m -= 1

        n -= 1

    return largest_palindrome

print find_largest_palindrome()
