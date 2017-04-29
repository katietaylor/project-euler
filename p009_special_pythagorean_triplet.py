
"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# (a ** 2) + (b ** 2) = (c ** 2)

# a + b > c
# a < b < c

# a + b + c = 1000


def get_pyth_triplet(total=1000):

    a = 1
    b = a + 1
    c = total - a - b

    while a < c:
        while c > b:
            triplet = (a, b, c)
            if (triplet[0] ** 2) + (triplet[1] ** 2) == (triplet[2] ** 2):
                print triplet
                return triplet[0] * triplet[1] * triplet[2]
            # print triplet
            b += 1
            c -= 1
        a += 1
        b = a + 1
        c = total - a - b

print get_pyth_triplet()
