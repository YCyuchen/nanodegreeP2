#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/20 10:39 AM 
# @Author : Yuchen 
# @File : Task1_Square_Root_of_Integer.py 
# @Software: PyCharm

"""
Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Error! Please enter valid number")
        return
    # Since the time complexity is O(log(n)), binary search algo should be considered
    left, right = 0, number

    while left <= right:
        center = (left + right) // 2
        if center ** 2 <= number < (center + 1) ** 2:
            return center

        else:
            if center ** 2 > number:
                right = center - 1
            else:
                left = center + 1


if __name__ == '__main__':
    # Task1 edge case, should return 0
    print("Pass" if (0 == sqrt(0)) else "Fail")

    # Task2 edge case, should return Assertion message
    sqrt(-1)

    # Task 3 normal test
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
