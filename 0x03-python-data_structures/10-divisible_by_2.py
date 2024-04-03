#!/usr/bin/python3
# 10-divisible_by_2.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>

def divisible_by_2(my_list=[]):
    return [True if x % 2 == 0 else False for x in my_list]