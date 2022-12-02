from random import randint


def gen_random(count, lower_bound, upper_bound):
    for i in range(count):
        yield(randint(lower_bound, upper_bound))

# print(*gen_random(5,1,3))