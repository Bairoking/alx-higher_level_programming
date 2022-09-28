#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    for sanna in set(my_list):
        result += sanna
    return result
