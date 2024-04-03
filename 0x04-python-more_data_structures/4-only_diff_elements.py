#!/usr/bin/python3
# 4-only_diff_elements.py
# Mohamed Kouchaoui <mohamed.kouchaoui19@gmail.com>
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return (set_1 ^ set_2)
