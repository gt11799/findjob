#! /usr/bin/env python
# _*_coding=utf8_*_
'''
Given a matrix, return the max sum of each column and each row
给定一个矩阵，返回不同行不同列的数的和的最大值。
豆瓣笔试题。
'''

from itertools import permutations
import random

def max_sum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    all_per = permutations(xrange(columns), columns)
    sum_list = []
    
    for each_turn in all_per:
        for idx in xrange(columns):
            sum_each = sum([matrix[row][each_turn[idx]] for row in xrange(rows)])
            sum_list.append(sum_each)
    return max(sum_list)
    
def test_max_sum():
    douban_matrix = []
    for _ in xrange(10):
        douban_matrix.append(range(10))
        
    print("test max_sum, with the increase turn: %s", max_sum(douban_matrix))
    
if __name__ == '__main__':
    test_max_sum()