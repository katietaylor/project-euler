
def sum_multiples_of_3_and_5():
    """If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000."""

    nums = range(1000)
    total = 0

    for num in nums:
        if num % 3 == 0:
            total += num
        elif num % 5 == 0:
            total += num

    return total
