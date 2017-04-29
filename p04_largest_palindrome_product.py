"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def find_largest_palindrome(high=999, low=100):

    palindromes = []
    n = high

    while n >= low:
        m = n

        while m >= low:
            product = n * m

            if str(product) == str(product)[::-1]:
                palindromes.append(product)
                break
            m -= 1
        n -= 1

    return max(palindromes)

print find_largest_palindrome()
