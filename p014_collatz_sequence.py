"""The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


def create_collatz_sequence(first_num):
    num = first_num
    collatz_sequence = []

    while num > 1:
        collatz_sequence.append(num)
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
    collatz_sequence.append(num)

    return len(collatz_sequence)


def find_longest_collatz_sequence(max_start=1000000):
    longest_collatz = 0
    longest_collatz_start = None

    for i in range(1, max_start):
        collatz_length = create_collatz_sequence(i)
        if collatz_length > longest_collatz:
            longest_collatz = collatz_length
            longest_collatz_start = i

    print "collatz length: ", collatz_length
    return longest_collatz_start

find_longest_collatz_sequence(1000000)
