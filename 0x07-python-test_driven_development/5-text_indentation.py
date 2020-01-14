#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    prints a text with 2 new lines

    """
    a = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == ":" or text[i] == "?" or text[i] == "." or a == 1:
            if a == 1 and text[i] not in (":", ".", "?"):
                if text[i] == " ":
                    continue
                else:
                    a = 0
                    print("{}".format(text[i]), end='')
            else:
                a = 1
                print("{}".format(text[i]), end='')
                print("\n")
        else:
            print("{}".format(text[i]), end='')
