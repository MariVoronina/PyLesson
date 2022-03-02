import math


def my_log(lst: list):
    return [None if i <= 0 else math.log(i) for i in lst]
