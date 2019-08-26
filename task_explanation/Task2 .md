# Task2 
## Problem description
You are given a sorted array which is rotated at some random pivot point. And you are given a target value to search. If found in the array return its index, otherwise return -1.
Eg: Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## Solution
Searching a sorted rotated array requires finding a pivot like element to help us know what particular half of our input array to search. A binary search algorithm will be implemented for this problem with slight modification. We will look at our two divided halfs to determine where the array is divided, knowing that each 1/2 will be sorted. 
I implement a mini binary search on each mini part . 

Time complexity for binary search is $O(log N)$ 
Space complexity is O(1) based on how many or "N" elements we have in our array.