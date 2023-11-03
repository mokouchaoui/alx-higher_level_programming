#!/usr/bin/python3
# 11-delete_at.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list