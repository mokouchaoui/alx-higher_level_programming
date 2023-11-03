#!/usr/bin/python3
# 5-no_c.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def no_c(my_string):
    new = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            new += i
    return new