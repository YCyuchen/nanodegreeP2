#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/25 9:22 PM 
# @Author : Yuchen 
# @File : Task6_Unsorted_integer_Array.py 
# @Software: PyCharm

"""
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
"""


def get_min_max(ints_list):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints_list(list): list of integers containing one or more integers
    """

    if len(ints_list) < 1:
        print("Num of elements in list must >0!")
        return

    min_int, max_int = ints_list[0], ints_list[0]
    for i in ints_list:
        if i < min_int:
            min_int = i
        if i > max_int:
            max_int = i
    output = (min_int, max_int)
    return output


## Example Test Case of Ten Integers
import random

# edge case: the inputlist is empty
# Test1 should return assertion
l = []
(get_min_max(l))

# Test2 should return (0,9)
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# edge case: the max and min are the same int
# Test3 should return (1,1)
l = [1 for _ in range(10)]
print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
