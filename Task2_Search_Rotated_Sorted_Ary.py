#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/22 9:10 AM 
# @Author : Yuchen 
# @File : Task2_Search_Rotated_Sorted_Ary.py 
# @Software: PyCharm


"""
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity
must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    low, high = 0, len(input_list) - 1  # index of left and right

    while low <= high:
        mid = (low + high) // 2

        if input_list[mid] == number:
            return mid

        elif input_list[low] <= input_list[mid]:
            if input_list[low] <= number <= input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

        elif input_list[low] > input_list[mid]:
            if input_list[mid] <= number <= input_list[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    # edge test, empty list should return -1
    test_function([[], 1])
    # edge test, sorted list should return 4
    test_function([[1,2,3,4,5], 5])

    # normal test
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

