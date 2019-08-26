#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/22 11:13 PM 
# @Author : Yuchen 
# @File : Task3_Rearrange_Array_Elements.py 
# @Software: PyCharm
"""

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list)
    list_len = len(input_list)
    assert len(sorted_list) > 1, "the element input_list is not enough! "
    print(sorted_list)
    bigger_num, small_num = '', ''
    for i in range(list_len - 2, -1, -2):
        small_num += str(sorted_list[i])

    for i in range(list_len - 1, -1, -2):
        bigger_num += str(sorted_list[i])

    print(int(bigger_num), int(small_num))
    return [int(bigger_num), int(small_num)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


if __name__ == '__main__':
    # Test1 edge case: should return [11,11]
    test_function([[1, 1, 1, 1], [11, 11]])

    # Test2 edge case: should return [100,10]
    test_function([[1, 1, 0, 0, 0], [100, 10]])

    # Test3 normal case:
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
