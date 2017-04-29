"""Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms."""


def create_fibonacci_nums(max_num=4000000):
    fibonacci_nums = [1, 1]
    next_value = 2

    while next_value <= max_num:
        fibonacci_nums.append(next_value)
        next_value = fibonacci_nums[-1] + fibonacci_nums[-2]

    return fibonacci_nums


def sum_even_fibonacci_nums(max_num=4000000):
    fibonacci_nums = create_fibonacci_nums(max_num)

    evens_total = 0

    for num in fibonacci_nums:
        if num % 2 == 0:
            evens_total += num

    return evens_total