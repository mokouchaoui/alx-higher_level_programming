#!/usr/bin/python3
# 5-no_c.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def no_c(my_string):
    return ''.join(ch for ch in my_string if ch not in ['c', 'C'])
