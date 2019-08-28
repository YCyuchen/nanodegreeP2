#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/23 9:40 AM 
# @Author : Yuchen 
# @File : Task4_Dutch_National_Flag_Problem.py 
# @Software: PyCharm


"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""


# version 1, cost more sapce complexity
def sort_012_v1(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    list1, list2, list3 = list(), list(), list()
    for i in input_list:
        if i == 0:
            list1.append(i)
        elif i == 1:
            list2.append(i)
        elif i == 2:
            list3.append(i)

    return list1 + list2 + list3


# version 2 ,better solution
def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012_v1(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    # Test1 , edge case: empty input list, should return []
    test_function([])

    # Test2 , edge case: only has two of the expected elements
    test_function([0, 0, 2, 2, 2])

    # Test3 , general test
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
