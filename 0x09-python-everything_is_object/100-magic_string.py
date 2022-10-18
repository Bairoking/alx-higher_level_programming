#!/usr/bin/python3
def magic_string():
    magic_string.sannaCount = getattr(magic_string, 'sannaCount', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.sannaCount)])
