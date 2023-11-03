#!/usr/bin/python3
# 9-max_integer.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def max_integer(my_list=[]):
        return (min(my_list, key=lambda i: -i)) if my_list else None
