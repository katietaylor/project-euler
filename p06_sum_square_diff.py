"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

nums = range(1, 101)

nums_squared = [n**2 for n in nums]
sum_of_squares = sum(nums_squared)

square_of_sums = sum(nums) ** 2

diff = square_of_sums - sum_of_squares
print diff
