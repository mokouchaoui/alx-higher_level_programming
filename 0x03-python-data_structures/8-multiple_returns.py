#!/usr/bin/python3
# 8-multiple_returns.py
# Mohamed Kouchaoui <mohamed.kouchaoui19gmail.com>
def multiple_returns(sentence):
    total = len(sentence)
    char = sentence[0] if total > 0 else "None"
    new = total, char
    return(new)