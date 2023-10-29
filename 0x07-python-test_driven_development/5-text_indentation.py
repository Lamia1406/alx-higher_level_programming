#!/usr/bin/python3
"""This module supplies one function, text_indentation(text)"""


def text_indentation(text):
    """prints a text with 2 new lines
        after each of these characters: ., ? and :"""
    if text is None or type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":":
            if text[i] == " ":
                continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
