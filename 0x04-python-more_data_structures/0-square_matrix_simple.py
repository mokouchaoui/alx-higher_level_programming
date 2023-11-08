#!/usr/bin/python3
# 0-square_matrix_simple.py
#Mohamed Kouchaoui <mohamed.kouchaoui19@gmail.com>
def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
    return squared
