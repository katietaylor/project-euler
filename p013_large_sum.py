"""Work out the first ten digits of the sum of one-hundred 50-digit
numbers (saved on p013.txt)."""


def create_list_of_nums():

    all_nums = open("p013.txt")

    nums = []

    for line in all_nums:
        data = line.rstrip()
        nums.append(data)
    all_nums.close()
    return nums

NUMBERS = create_list_of_nums()


def sum_num_column(idx):

    total = 0
    for num in NUMBERS:
        total += int(num[idx])

    return total


def get_column_totals():

    values = []
    remainder = 0
    for i in range(49, -1, -1):
        column = sum_num_column(i)
        total_value = str(column + remainder)
        values.append(int(total_value[-1]))
        remainder = int(total_value[:-1])

    for value in list(str(remainder))[::-1]:
        values.append(int(value))

    # only need to return first 10 digits
    return values[-1:-11:-1]
