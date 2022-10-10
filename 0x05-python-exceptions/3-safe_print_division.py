#!/usr/bin/python3
def safe_print_division(sanna, sira):
    """Returns the division of sanna by sira."""
    try:
        div = sanna / sira
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
