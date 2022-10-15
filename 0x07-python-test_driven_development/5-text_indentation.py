#!/usr/bin/python3
"""
This module contains a function that indents texts
"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sannaCount = 0
    while sannaCount < len(text) and text[sannaCount] == " ":
        sannaCount = sannaCount + 1

    while sannaCount < len(text):
        print(text[sannaCount], end="")
        if text[sannaCount] == "\n" or text[sannaCount] in ".?:":
            if text[sannaCount] in ".?:":
                print("\n")
            sannaCount = sannaCount + 1
            while sannaCount < len(text) and text[sannaCount] == " ":
                sannaCount = sannaCount + 1
            continue
        sannaCount = sannaCount + 1
