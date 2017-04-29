"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""


def sum_primes(max_prime=2000000):

    nums = range(2, max_prime + 1)
    idx = 0

    while nums[idx] < max_prime ** 0.5 + 1:
        nums = [num for num in nums if num % nums[idx] != 0 or num == nums[idx]]
        idx += 1
    return sum(nums)

print sum_primes()



# note: began be adapting solution from problem 7, and that took 1 min to run
# changed the solution to create list and then reduce it down to only primes
# I believe this mean n log(n) instead of the other n^2 solution
