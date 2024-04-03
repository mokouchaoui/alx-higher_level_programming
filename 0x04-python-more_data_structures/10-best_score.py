#!/usr/bin/python3
# 10-best_score.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
