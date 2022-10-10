#!/usr/bin/python3
def list_division(sanna_1, sanna_2, sira):
    """Divides two lists element by element.
    Args:
        sanna_1 (list): The first list.
        sanna_2 (list): The second list.
        sira (int): The number of elements to divide.
    Returns:
        A new list of length sira containing all the divisions.
    """
    new_list = []
    for i in range(0, sira):
        try:
            div = sanna_1[i] / sanna_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
