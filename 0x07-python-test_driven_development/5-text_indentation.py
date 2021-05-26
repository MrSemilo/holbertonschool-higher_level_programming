#!/usr/bin/python3
""" Indentation """


def text_indentation(text):
    """ Indent """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    vari = 1
    for l in text:
        if vari is 1 and l is " ":
            pass
        else:
            print(l, end="")
            vari = 0
        if l is '.' or l is '?' or l is ':':
            print("\n")
            vari = 1
