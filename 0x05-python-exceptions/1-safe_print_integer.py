#!/usr/bin/python3
def safe_print_integer(sanna):
    try:
        print("{:d}".format(sanna))
        return True
    except (ValueError, TypeError):
        return False
