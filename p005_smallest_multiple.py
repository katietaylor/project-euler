"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"""


# solution works, but not well optimized
def find_smallest_multiple(max):

    factors = range(1, max + 1)
    multiplier = factors[-2]
    num = factors[-1] * multiplier
    factors = factors[::-1]

    while True:
        for factor in factors:
            if num % factor != 0:
                multiplier += 1
                num = factors[0] * multiplier
                break
            elif factor == factors[-1]:
                return num

print find_smallest_multiple(20)
