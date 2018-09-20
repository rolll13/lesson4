import random
from math import pi


def generator(quantity):
    i = 0
    quant_trys = quantity
    while quantity > 0:
        quantity -= 1
        random_num = random.randint(0, 100) % 2
        if random_num == 0:
            i += 1
    return int(i / quant_trys * 100)


def circle(radius):
    return pi * radius ** 2


def triangle(base, height):
    return base / 2 * height


def rectangle(length, width):
    return length * width
